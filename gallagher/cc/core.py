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
from typing import Optional
from datetime import datetime
from dataclasses import dataclass

from http import HTTPStatus  # Provides constants for HTTP status codes

import httpx

from gallagher.exception import (
    UnlicensedFeatureException
)

from ..dto.utils import (
    AppBaseModel,
)

from ..dto.detail import (
    FeaturesDetail,
)

from ..dto.response import (
    DiscoveryResponse,
)

from ..exception import (
    UnlicensedFeatureException,
    NotFoundException,
    AuthenticationError,
)


def check_api_key_format(api_key):
    """ Validates that the Gallagher Key is in the right format.

    It's not possible for the API client to validate the key against
    Gallagher servers but it will validate that the key is in the
    right format.
    """
    api_tokens = api_key.split('-')
    return (api_tokens.count() == 8)


def get_authorization_headers():
    """ Creates an authorization header for Gallagher API calls

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
        'Content-Type': 'application/json',
        'Authorization': f'GGL-API-KEY {api_key}'
    }


@dataclass
class EndpointConfig:
    """ A configuration for an API endpoint

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
    # fields: list[str] = []  # Optional list of fields

    @classmethod
    async def validate_endpoint(cls):
        """ Check to see if the feature is licensed and available

        Gallagher REST API is licensed per feature, if a feature is not
        the endpoint is set to none and we should throw an exception
        """
        if not cls.endpoint:
            raise UnlicensedFeatureException(
                "Endpoint not defined"
            )


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
    # This value is memoized and should perform
    CURRENT = DiscoveryResponse(
        version="0.0.0",  # Indicates that it's not been discovered
        features=FeaturesDetail()
    )


class APIEndpoint:
    """ Base class for all API objects

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
        """ Expires endpoint discovery information

        Use this with caution as it significantly increases roundtrip times
        and decreases API client performance.

        Unless the server instance updates mid cycle, there should be no
        reason for these discovered URLs to change.
        """
        Capabilities.CURRENT = DiscoveryResponse(
           version="0.0.0",  # Indicates that it's not been discovered
            features=FeaturesDetail()
        )

    @classmethod
    async def get_config(cls) -> EndpointConfig:
        """ Returns the configuration for the endpoint

        This method can be overridden by the child class to
        provide additional configuration options.
        """
        raise NotImplementedError(
            "get_config method not implemented"
        )

    @classmethod
    async def _discover(cls):
        """ The Command Centre root API endpoint 

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
        """

        if Capabilities.CURRENT.version != "0.0.0" and\
                type(Capabilities.CURRENT._good_known_since) is datetime:
            # We've already discovered the endpoints as per HATEOAS
            # design requirement, however because the endpoint configuration is
            # dynamically populated, we have to call the get_config method
            cls.__config__ = await cls.get_config()
            return

        # Auto-discovery of the API endpoints, this will
        # be called as part of the bootstrapping process
        from . import api_base
        async with httpx.AsyncClient() as _httpx_async:
            response = await _httpx_async.get(
                api_base,
                headers=get_authorization_headers(),
            )

            await _httpx_async.aclose()

            parsed_obj = DiscoveryResponse.model_validate(
                response.json()
            )

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
            # an instance of a pyndatic object and all values are thus
            # copied not referenced.
            cls.__config__ = await cls.get_config()

    @classmethod
    async def list(cls, skip=0):
        """ For a list of objects for the given resource

        Most resources can be searched which is exposed by this method.
        Resources also allow pagination which can be controlled by the skip

        :param int skip: fetch responses from this anchor
        """
        await cls._discover()

        async with httpx.AsyncClient() as _httpx_async:

            try:

                response = await _httpx_async.get(
                    f'{cls.__config__.endpoint.href}',
                    headers=get_authorization_headers(),
                )

                await _httpx_async.aclose()

                if response.status_code == HTTPStatus.OK:

                    parsed_obj = cls.__config__.dto_list.model_validate(
                        response.json()
                    )

                    return parsed_obj

                elif response.status_code == HTTPStatus.FORBIDDEN:
                    raise UnlicensedFeatureException()
                elif response.status_code == HTTPStatus.UNAUTHORIZED:
                    raise AuthenticationError()

            except httpx.RequestError as e:
                pass

    @classmethod
    async def retrieve(cls, id):
        """ Retrieve a single object for the given resource

        Most objects have an ID which is numeral or UUID. 
        Each resource also provides a href and pagination for
        children.

        :param int id: identifier of the object to be fetched
        """
        await cls._discover()

        async with httpx.AsyncClient() as _httpx_async:

            try:

                response = await _httpx_async.get(
                    f'{cls.__config__.endpoint.href}/{id}',
                    headers=get_authorization_headers(),
                )

                await _httpx_async.aclose()

                if response.status_code == HTTPStatus.OK:

                    parsed_obj = cls.__config__.dto_retrieve.model_validate(
                        response.json()
                    )

                    return parsed_obj

                elif response.status_code == HTTPStatus.NOT_FOUND:
                    raise NotFoundException()
                elif response.status_code == HTTPStatus.FORBIDDEN:
                    raise UnlicensedFeatureException()
                elif response.status_code == HTTPStatus.UNAUTHORIZED:
                    raise AuthenticationError()

            except httpx.RequestError as e:
                pass

    @classmethod
    async def modify(cls):
        """

        """
        pass

    @classmethod
    async def create(cls, **params):
        """

        """
        cls._discover()

    @classmethod
    async def delete(cls):
        """

        """
        cls._discover()

    @classmethod
    async def search(
        cls,
        top: int = 100,
        sort: str = 'id',
        fields: str = 'defaults',
        **kwargs
    ):
        """ Search wrapper for most objects to dynamically search content

        Each object has a set of fields that you can query for, most searches
        also allow you to search for a partial string.

        :param int top: Number of results to return
        :param str sort: Sort order, can be set to id or -id
        :param str fields: List of fields to return
        :param kwargs: Fields to search for

        """
        await cls._discover()

        params = {
            'top': top,
            'sort': sort,
            'fields': fields,
        }

        # Adds arbitrary fields to the search, these will be different
        # for each type of object that calls the base function
        params.update(kwargs)

        async with httpx.AsyncClient() as _httpx_async:

            response = await _httpx_async.get(
                f'{cls.__config__.endpoint.href}',
                params=params,
                headers=get_authorization_headers(),
            )

            await _httpx_async.aclose()

            parsed_obj = cls.__config__.dto_list.model_validate(
                response.json()
            )

            return parsed_obj
        
    # Proposed methods for internal use    
    @classmethod
    async def _get_all(
        cls, 
        url:str, 
        response_class: AppBaseModel | None,
    ):
        """
        """

        await cls._discover()

        async with httpx.AsyncClient() as _httpx_async:

            try:

                response = await _httpx_async.get(
                    url,
                    headers=get_authorization_headers(),
                )

                await _httpx_async.aclose()

                if response.status_code == HTTPStatus.OK:

                    if not response_class:
                        return

                    parsed_obj = response_class.model_validate(
                        response.json()
                    )

                    return parsed_obj

                elif response.status_code == HTTPStatus.FORBIDDEN:
                    raise UnlicensedFeatureException()
                elif response.status_code == HTTPStatus.UNAUTHORIZED:
                    raise AuthenticationError()

            except httpx.RequestError as e:
                pass

    @classmethod
    async def _post(
        cls, 
        url: str,
        payload: AppBaseModel | None,
        response_class: AppBaseModel | None = None,
    ):
        """
        """

        await cls._discover()

        async with httpx.AsyncClient() as _httpx_async:

            try:

                response = await _httpx_async.post(
                    url,
                    json=payload.dict() if payload else None,
                    headers=get_authorization_headers(),
                )

                await _httpx_async.aclose()

                if response.status_code == HTTPStatus.OK:

                    if not response_class:
                        return

                    parsed_obj = response_class.model_validate(
                        response.json()
                    )

                    return parsed_obj

                elif response.status_code == HTTPStatus.FORBIDDEN:
                    raise UnlicensedFeatureException()
                elif response.status_code == HTTPStatus.UNAUTHORIZED:
                    raise AuthenticationError()

            except httpx.RequestError as e:
                raise(e)
