""" Utilities for the Gallagher Command Centre API

This package provides a set of utilities that are used that each endpoint
uses to communicate with the Gallagher Command Centre API.

Every endpoint inherits from the APIEndpoint class and must define
a configuration that is assigned to the variable __config__.

The endpoint variable in the EndpointConfig should be assigned to a reference
to the endpoint in the DiscoveryResponse object. When initialised the
endpoint will be assigned to None but will self heal as part of 
the bootstrapping process.
"""

from typing import (
    Optional,
    Tuple,
    Any,
    List,
)

from datetime import datetime
from dataclasses import dataclass

from http import HTTPStatus  # Provides constants for HTTP status codes

import httpx

from . import proxy as proxy_address
from gallagher.exception import UnlicensedFeatureException

from ..dto.utils import (
    AppBaseModel,
    AppBaseResponseWithFollowModel,
)

from ..dto.detail import (
    FeaturesDetail,
)

from ..dto.response import (
    DiscoveryResponse,
)

from ..enum import (
    SearchSortOrder,
)

from ..exception import (
    UnlicensedFeatureException,
    NotFoundException,
    AuthenticationError,
    DeadEndException,
    PathFollowNotSupportedError,
)


def _check_api_key_format(api_key):
    """Validates that the Gallagher Key is in the right format.

    It's not possible for the API client to validate the key against
    Gallagher servers but it will validate that the key is in the
    right format.
    """
    api_tokens = api_key.split("-")
    return api_tokens.count() == 8


def _sanitise_name_param(name: str) -> str:
    """
    Limits the returned items to those with a name that matches this string. 
    Without surrounding quotes or a percent sign or underscore, 
    it is a substring match; surround the parameter with double quotes "..." 
    for an exact match. Without quotes, a percent sign % will match any substring 
    and an underscore will match any single character.
    """
    if name.startswith('"') and name.endswith('"'):
        return name

    if name.startswith("%") or name.startswith("_"):
        return name

    return f"%{name}%"

def _get_authorization_headers():
    """Creates an authorization header for Gallagher API calls

    The server expects an Authorization header with GGL-API-KEY
    set to the API key provided by Gallagher Command Centre.

    This API key is what allows the cloud proxy to determine where
    the request should be routed to.

    See the Authorization section here for more information
    https://gallaghersecurity.github.io/cc-rest-docs/ref/events.html

    from gallagher import cc, const

    cc.api_key = "GH_"

    """
    from . import api_key

    return {
        "Content-Type": "application/json",
        "Authorization": f"GGL-API-KEY {api_key}",
    }


@dataclass
class EndpointConfig:
    """A configuration for an API endpoint

    Each API endpoint has a configuration that defines how
    the APIBase should attempt to parse responses from the
    Gallagher servers.

    Additionally it provides defaults for various parameters
    that are commonly accepted by endpoints.

    Not assigning a configuration to an endpoint will result
    in APIBase raising an exception.

    The configuration is assigned a special variable called
    __config__ which is set to None by default.

    """

    endpoint: str  # partial path to the endpoint e.g. day_category
    dto_list: Optional[any] = None  # DTO to be used for list requests
    dto_retrieve: Optional[any] = None  # DTO to be used for retrieve requests

    top: Optional[int] = 10  # Number of response to download
    sort: Optional[str] = "id"  # Can be set to id or -id

    fields: Tuple[str] = ()  # Optional list of fields, blank = all
    search: Tuple[str] = () # If the endpoint supports search, blank = none

    @classmethod
    async def validate_endpoint(cls):
        """Check to see if the feature is licensed and available

        Gallagher REST API is licensed per feature, if a feature is not
        the endpoint is set to none and we should throw an exception
        """
        if not cls.endpoint:
            raise UnlicensedFeatureException("Endpoint not defined")


class Capabilities:

    # Discover response object, each endpoint will reference
    # one of the instance variable Href property to get the
    # path to the endpoint.
    #
    # Gallagher recommends that the endpoints not be hardcoded
    # into the client and instead be discovered at runtime.
    #
    # Note that if a feature has not been licensed by a client
    # then the path will be set to None, if the client attempts
    # to access the endpoint then the library will throw an exception
    #
    # This value is memoized and should be performant
    CURRENT = DiscoveryResponse(
        version="0.0.0",  # Indicates that it's not been discovered
        features=FeaturesDetail(),
    )

class APIEndpoint:
    """Base class for all API objects

    All API endpoints must inherit from this class and provide a Config class
    that automates the implementation of many of the API methods.

    If the endpoints provide additional methods then they are to implement them
    based on the same standards as this base class.

    """

    # Do not set this variable in your class, this is set by the
    # lifecycle methods and use to cache the configuration object
    __config__ = None

    @classmethod
    async def expire_discovery(cls):
        """Expires endpoint discovery information

        Use this with caution as it significantly increases roundtrip times
        and decreases API client performance.

        Unless the server instance updates mid cycle, there should be no
        reason for these discovered URLs to change.
        """
        Capabilities.CURRENT = DiscoveryResponse(
            version="0.0.0",  # Indicates that it's not been discovered
            features=FeaturesDetail(),
        )

    @classmethod
    async def get_config(cls) -> EndpointConfig:
        """Returns the configuration for the endpoint

        This method can be overridden by the child class to
        provide additional configuration options.
        """
        raise NotImplementedError("get_config method not implemented")

    @classmethod
    async def _discover(cls):
        """The Command Centre root API endpoint

        Much of Gallagher's API documentation suggests that we don't
        hard code the URL, but instead use the discovery endpoint by
        calling the root endpoint.

        This should be a singleton which is instantiated upon initialisation
        and then used across the other endpoints.

        For example features.events.events.href is the endpoint for the events
        where as features.events.events.updates is the endpoint for getting
        updates to the changes to events.

        This differs per endpoint that we work with.

        Note that references to Capabilities.CURRENT as a singleton, while
        cls.method when executing a class method.

        :params class cls: The class that is calling the method
        """

        if Capabilities.CURRENT.version != "0.0.0" and isinstance(
            Capabilities.CURRENT._good_known_since, datetime
        ):
            # We've already discovered the endpoints as per HATEOAS
            # design requirement, however because the endpoint configuration is
            # dynamically populated, we have to call the get_config method
            cls.__config__ = await cls.get_config()
            return

        # Auto-discovery of the API endpoints, this will
        # be called as part of the bootstrapping process
        from . import api_base

        async with httpx.AsyncClient(proxy=proxy_address) as _httpx_async:
            # Don't use the _get wrapper here, we need to get the raw response
            response = await _httpx_async.get(
                api_base,
                headers=_get_authorization_headers(),
            )

            await _httpx_async.aclose()

            parsed_obj = DiscoveryResponse.model_validate(response.json())

            # Assign the capabilities to the class, this should
            # result in the endpoint
            #
            # With the refactored initialisation of the pydantic
            # models, the values for the unavailable endpoints
            # should be set to None
            Capabilities.CURRENT = parsed_obj

            # Set this so the configuration is only discovered
            # once per endpoint
            #
            # If we assign the __config__ variable in the class
            # that inherits from this class, the instance of EndpointConfig
            # will copy the None values from the Capabilities.CURRENT
            # object, this primarily because Capabilities.CURRENT is
            # an instance of a pydantic object and all values are thus
            # copied not referenced.
            cls.__config__ = await cls.get_config()


    @classmethod
    async def list(cls, skip=0):
        """For a list of objects for the given resource

        Most resources can be searched which is exposed by this method.
        Resources also allow pagination which can be controlled by the skip

        :param int skip: fetch responses from this anchor
        """
        await cls._discover()  # Discover must be here for dynamic config

        return await cls._get(
            cls.__config__.endpoint.href,
            cls.__config__.dto_list,
        )

    @classmethod
    async def retrieve(cls, id):
        """Retrieve a single object for the given resource

        Most objects have an ID which is numeral or UUID.
        Each resource also provides a href and pagination for
        children.

        :param int id: identifier of the object to be fetched
        """
        await cls._discover()  # Discover must be here for dynamic config

        return await cls._get(
            f"{cls.__config__.endpoint.href}/{id}",
            cls.__config__.dto_retrieve,
        )

    @classmethod
    async def modify(cls):
        """ """
        pass

    @classmethod
    async def create(cls, **params):
        """ """
        cls._discover()

    @classmethod
    async def delete(cls):
        """ """
        cls._discover()

    @classmethod
    async def search(
        cls,
        sort: SearchSortOrder = SearchSortOrder.ID,
        top: int = 100,
        name: Optional[str] = None, # TODO: en
        division: str = None, # TODO: use division type
        direct_division: str = None, # TODO: use division type
        description: Optional[str] = None,
        fields: str | List[str] = "defaults",
        **kwargs,
    ):
        """Search wrapper for most objects to dynamically search content

        We typically use the detail endpoint to run the query once the parameters
        have been constructed from the set defined in this method, and any
        extras that are passed as part of the kwargs.

        direct_division is a division whos ancestors are not included in the search

        :param int top: Number of results to return
        :param str sort: Sort order, can be set to id or -id
        :param str name: Name of the object to search for
        :param str division: Division to search for
        :param str direct_division: Direct division to search for
        :param str description: Description to search for
        :param str fields: List of fields to return
        :param kwargs: Fields to search for

        """
        await cls._discover()

        params = {
            "top": top,
            "sort": sort,
            "fields": fields,
        }

        if name:
            params["name"] = name

        if division:
            params["division"] = division

        if direct_division:
            params["directDivision"] = direct_division

        if description:
            params["description"] = description

        # Adds arbitrary fields to the search, these will be different
        # for each type of object that calls the base function
        params.update(kwargs)

        return await cls._get(
            cls.__config__.endpoint.href,
            cls.__config__.dto_list,
            params=params,
        )


    # Follow links methods, these are valid based on if the response
    # classes make available a next, previous or update href, otherwise
    # the client raises an NotImplementedError

    @classmethod
    async def next(cls, response):
        """Fetches the next set of results

        This is only valid if the response object has a next href
        """
        await cls._discover()

        # If the cls.__config__ is not of type AppBaseResponseWithFollowModel
        # then we should raise an exception
        if not issubclass(cls.__config__.dto_list, AppBaseResponseWithFollowModel):
            """A response model must have a next, previous or update"""
            raise PathFollowNotSupportedError(
                "Endpoint does not support previous, next or updates"
            )

        if not response.next:
            """We have no where to go based on the passed response"""
            raise DeadEndException("No further paths to follow for this endpoint")

        return await cls._get(
            response.next.href,
            cls.__config__.dto_list,
        )

    @classmethod
    async def previous(cls, response):
        """Fetches the previous set of results

        This is only valid if the response object has a previous href
        """
        await cls._discover()

        # If the cls.__config__ is not of type AppBaseResponseWithFollowModel
        # then we should raise an exception
        if not issubclass(cls.__config__.dto_list, AppBaseResponseWithFollowModel):
            """A response model must have a next, previous or update"""
            raise PathFollowNotSupportedError(
                "Endpoint does not support previous, next or updates"
            )

        if not response.previous:
            raise DeadEndException("No path leads further back than this")

        return await cls._get(
            cls.response.previous.href,
            cls.__config__.dto_list,
        )

    @classmethod
    async def poll(cls, response):
        """Fetches the updated set of results

        Update follow the same pattern as next and previous, except
        it keeps yielding results until the server has no more updates
        """
        await cls._discover()

        # If the cls.__config__ is not of type AppBaseResponseWithFollowModel
        # then we should raise an exception
        if not issubclass(cls.__config__.dto_list, AppBaseResponseWithFollowModel):
            """A response model must have a next, previous or update"""
            raise PathFollowNotSupportedError(
                "Endpoint does not support previous, next or updates"
            )

        return await cls._get(
            cls.response.update.href,
            cls.__config__.dto_list,
        )

    # Proposed methods for internal use
    @classmethod
    async def _get(
        cls,
        url: str,
        response_class: AppBaseModel | None,
        params: dict[str, Any] = {},
    ):
        """Generic _get method for all endpoints

        This is to be used if we can find a prepared url endpoint, this
        is useful for follow on endpoints like commenting, next, previous
        etc. The response_class is used to parse the returned object.

        Note: that this does not run discover as it expects the endpoint to
        be fully formed and callable. If you are calling this from a generic
        endpoint like `list` please ensure you've called _discover first.

        :param str url: URL to fetch the data from
        :param AppBaseModel response_class: DTO to be used for list requests
        """
        async with httpx.AsyncClient(proxy=proxy_address) as _httpx_async:

            try:

                response = await _httpx_async.get(
                    f"{url}",  # required to turn pydantic object to str
                    headers=_get_authorization_headers(),
                    params=params,
                )

                await _httpx_async.aclose()

                if response.status_code == HTTPStatus.OK:

                    if not response_class:
                        return

                    parsed_obj = response_class.model_validate(response.json())

                    return parsed_obj

                elif response.status_code == HTTPStatus.NOT_FOUND:
                    raise NotFoundException()
                elif response.status_code == HTTPStatus.FORBIDDEN:
                    raise UnlicensedFeatureException()
                elif response.status_code == HTTPStatus.UNAUTHORIZED:
                    raise AuthenticationError()

            except httpx.RequestError as e:
                raise (e)

    @classmethod
    async def _post(
        cls,
        url: str,
        payload: AppBaseModel | None,
        response_class: AppBaseModel | None = None,
    ):
        """ Generic POST wrapper with error handling

        Use this internally for all POST requests, this will handle
        exception handling and configuration of proxies.

        The behaviour is very similar to the _get method, except
        parsing and sending out a body as part of the request. 
        """
        async with httpx.AsyncClient(proxy=proxy_address) as _httpx_async:

            try:

                response = await _httpx_async.post(
                    f"{url}",  # required to turn pydantic object to str
                    json=payload.model_dump() if payload else None,
                    headers=_get_authorization_headers(),
                )

                await _httpx_async.aclose()

                if response.status_code == HTTPStatus.OK:

                    if not response_class:
                        # TODO: should this return a boolean?
                        """No response to parse"""
                        return True

                    parsed_obj = response_class.model_validate(response.json())

                    return parsed_obj

                elif response.status_code == HTTPStatus.FORBIDDEN:
                    raise UnlicensedFeatureException()
                elif response.status_code == HTTPStatus.UNAUTHORIZED:
                    raise AuthenticationError()

            except httpx.RequestError as e:
                raise (e)
