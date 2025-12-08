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
from pathlib import Path
from dataclasses import dataclass

from asyncio import Event as AsyncioEvent  # Used for signalling events

from http import HTTPStatus  # Provides constants for HTTP status codes

import ssl
import httpx

from pydantic_settings import BaseSettings
from pydantic import (
    Field,
    HttpUrl,
)

from gallagher.exception import UnlicensedFeatureException

from ..const import (
    TRANSPORT,
    URL,
)

from ..dto.utils import (
    AppBaseModel,
    AppBaseResponseWithFollowModel,
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
    NoAPIKeyProvidedError,
)

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

class RequestHeadersMixin():
    """Mixin to provide request headers for Gallagher API calls
    
    Reason for this being a mixin is to allow both the APIClient and
    APIEndpoint to share the same method for generating headers.
    """

    def _check_api_key_format(api_key):
        """Validates that the Gallagher Key is in the right format.

        It's not possible for the API client to validate the key against
        Gallagher servers but it will validate that the key is in the
        right format.
        """
        api_tokens = api_key.split("-")
        return len(api_tokens) == 8

    def _get_authorization_headers(self):
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
        from .. import __version__

        if not self.config.api_key:
            """ API key cannot be empty

            Trap this exception to ensure that you have configured the
            client properly.
            """
            raise NoAPIKeyProvidedError()

        if not self._check_api_key_format(self.config.api_key):
            """ API key is not in the right format

            The API key is not in the right format, this is likely because
            the client has not copied the key correctly from the Gallagher
            Command Centre.
            """
            raise ValueError("API key is not in the right format")

        return {
            "Content-Type": "application/json",
            "User-Agent": f"GallagherPyToolkit/{__version__}",
            "Authorization": f"GGL-API-KEY {self.config.api_key}",
        }
    

class CommandCentreConfig(BaseSettings):
    """ Configuration for Command Centre API client """

    # Follow the instructions in the Gallagher documentation
    # to obtain an API key
    api_key: str = Field(
        ...,
        description="API key for Command Centre REST API",
    )

    # Certificate file to be used for authentication
    file_tls_certificate: Optional[Path] = None

    # Private key file to be used for authentication
    file_private_key: Optional[Path] = None

    # By default the base API is set to the Australian Gateway
    # Override this with the US gateway or a local DNS/IP address
    api_base: HttpUrl = Field(
        default=URL.CLOUD_GATEWAY_AU,
        description="Base URL for Command Centre REST API",
    )   

    # Default is set to the library, set this to your application
    client_id: str = Field(
        default="gallagher-py",
        description="Client ID for Command Centre REST API",
    )

    # By default connections are sent straight to the server
    # should you wish to use a proxy, set this to the proxy URL
    proxy: Optional[HttpUrl] = Field(
        default=None,
        description="Proxy URL for Command Centre REST API",
    )

    @property
    def ssl_context(self):
        """Returns the SSL context for the endpoint

        This method can be overridden by the child class to
        provide additional SSL context options.
        """
        from . import file_tls_certificate, file_private_key

        if not file_tls_certificate:
            """TLS certificate is required for SSL context"""
            return None

        context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        context.load_cert_chain(file_tls_certificate, file_private_key)
        return context

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
    endpoint_follow: str | None = None  # partial path to the follow endpoint

    dto_follow: Optional[any] = None  # DTO to be used for follow requests
    dto_list: Optional[any] = None  # DTO to be used for list requests
    dto_retrieve: Optional[any] = None  # DTO to be used for retrieve requests

    top: int = 10  # Number of response to download
    sort: str = "id"  # Can be set to id or -id

    fields: Tuple[str] = ()  # Optional list of fields, blank = all
    search: Tuple[str] = ()  # If the endpoint supports search, blank = none

    async def validate_endpoint(self):
        """Check to see if the feature is licensed and available

        Gallagher REST API is licensed per feature, if a feature is not
        the endpoint is set to none and we should throw an exception
        """
        if not self.endpoint:
            raise UnlicensedFeatureException("Endpoint not defined")

class APIEndpoint(RequestHeadersMixin,):
    """Base class for all API objects

    All API endpoints must inherit from this class and provide a Config class
    that automates the implementation of many of the API methods.

    If the endpoints provide additional methods then they are to implement them
    based on the same standards as this base class.

    """

    # Do not set this variable in your class, this is set by the
    # lifecycle methods and use to cache the configuration object
    __config__ = None

    def __init__(self, config: CommandCentreConfig, capabilities: DiscoveryResponse):
        """Initialises the API endpoint with the discovery response

        Each endpoint requires the discovery response to be passed
        in so that it can dynamically assign the endpoint hrefs
        based on what the server provides.

        :param CommandCentreConfig config: The API client configuration
        :param DiscoveryResponse capabilities: The discovery response
        """
        self.config = config
        self._CAPABILITIES = capabilities

        # Unlike before gallagher/#96 we now call get_config
        # here as discover would have already completed
        self.__config__ = self.get_config()


    def get_config(self) -> EndpointConfig:
        """Returns the configuration for the endpoint

        This method can be overridden by the child class to
        provide additional configuration options.

        Note: since gallagher/#96 this was refactored to be
        a sync method so it can be called in the constructor.
        """
        raise NotImplementedError("get_config method not implemented")

    async def list(self, skip=0):
        """For a list of objects for the given resource

        Most resources can be searched which is exposed by this method.
        Resources also allow pagination which can be controlled by the skip

        :param int skip: fetch responses from this anchor
        """
        return await self._get(
            self.__config__.endpoint.href,
            self.__config__.dto_list,
        )

    async def retrieve(self, id):
        """Retrieve a single object for the given resource

        Most objects have an ID which is numeral or UUID.
        Each resource also provides a href and pagination for
        children.

        :param int id: identifier of the object to be fetched
        """
        return await self._get(
            f"{self.__config__.endpoint.href}/{id}",
            self.__config__.dto_retrieve,
        )

    async def modify(self):
        """ """
        pass

    async def create(self, **params):
        """ """
        pass

    async def delete(self):
        """ """
        pass

    async def search(
        self,
        sort: SearchSortOrder = SearchSortOrder.ID,
        top: int = 100,
        name: Optional[str] = None,  # TODO: en
        division: str = None,  # TODO: use division type
        direct_division: str = None,  # TODO: use division type
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

        return await self._get(
            self.__config__.endpoint.href,
            self.__config__.dto_list,
            params=params,
        )

    # Follow links methods, these are valid based on if the response
    # classes make available a next, previous or update href, otherwise
    # the client raises an NotImplementedError

    async def next(self, response):
        """Fetches the next set of results

        This is only valid if the response object has a next href
        """
        # If the self.__config__ is not of type AppBaseResponseWithFollowModel
        # then we should raise an exception
        if not issubclass(self.__config__.dto_list, AppBaseResponseWithFollowModel):
            """A response model must have a next, previous or update"""
            raise PathFollowNotSupportedError(
                "Endpoint does not support previous, next or updates"
            )

        if not response.next:
            """We have no where to go based on the passed response"""
            raise DeadEndException(
                "No further paths to follow for this endpoint")

        return await self._get(
            response.next.href,
            self.__config__.dto_list,
        )

    async def previous(self, response):
        """Fetches the previous set of results

        This is only valid if the response object has a previous href
        """
        # If the self.__config__ is not of type AppBaseResponseWithFollowModel
        # then we should raise an exception
        if not issubclass(self.__config__.dto_list, AppBaseResponseWithFollowModel):
            """A response model must have a next, previous or update"""
            raise PathFollowNotSupportedError(
                "Endpoint does not support previous, next or updates"
            )

        if not response.previous:
            raise DeadEndException("No path leads further back than this")

        return await self._get(
            self.response.previous.href,
            self.__config__.dto_list,
        )

    async def follow(
        self,
        asyncio_event: AsyncioEvent,  # Not to be confused with Gallagher event
        params: dict[str, Any] = {},
    ):
        """Fetches update and follows next to get the next set of results

        parameters:
        - event: asyncio.Event object to signal when to stop
        - params: dictionary of parameters to pass to the endpoint

        Long poll behaviour in the Gallagher API uses the following pattern:
        - The request will wait until there's a new set of changes
        - If no changes are detected in 30 seconds then the server returns
          a blank response with a new next link
        - Follow the next link to get the next set of changes
        - This repeats until you stop listening

        This behaviour is followed by updates and changes endpoints, this method
        should be used a helper for the updates and changes methods.
        """
        if not self.__config__.endpoint_follow:
            raise PathFollowNotSupportedError(
                "Endpoint does not support previous, next or updates"
            )

        # Initial url is set to endpoint_follow
        url = f"{self.__config__.endpoint_follow.href}"

        async with httpx.AsyncClient(
            proxy=self.config.proxy,
            verify=self.config.ssl_context,
        ) as _httpx_async:

            while not asyncio_event.is_set():
                try:
                    response = await _httpx_async.get(
                        f"{url}",  # required to turn pydantic object to str
                        headers=self._get_authorization_headers(),
                        params=params,
                        timeout=TRANSPORT.TIMEOUT_POLL,
                    )

                    if response.status_code == HTTPStatus.OK:

                        parsed_obj = self.__config__.dto_follow.model_validate(
                            response.json()
                        )

                        # send this back to the caller
                        yield parsed_obj

                        if not parsed_obj.next:
                            return

                        # set the url to the next follow and we should
                        # be able to follow this endlessly
                        url = f"{parsed_obj.next.href}"

                    elif response.status_code == HTTPStatus.NOT_FOUND:
                        raise NotFoundException()
                    elif response.status_code == HTTPStatus.FORBIDDEN:
                        raise UnlicensedFeatureException()
                    elif response.status_code == HTTPStatus.UNAUTHORIZED:
                        raise AuthenticationError()

                except httpx.RequestError as e:
                    raise (e)

    async def _get(
        self,
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
        async with httpx.AsyncClient(
            proxy=self.config.proxy,
            verify=self.config.ssl_context,
        ) as _httpx_async:

            try:

                response = await _httpx_async.get(
                    f"{url}",  # required to turn pydantic object to str
                    headers=self._get_authorization_headers(),
                    params=params,
                )

                await _httpx_async.aclose()

                if response.status_code == HTTPStatus.OK:

                    if not response_class:
                        return

                    parsed_obj = response_class.model_validate(
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
                raise (e)

    async def _post(
        self,
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
        async with httpx.AsyncClient(
            proxy=self.config.proxy,
            verify=self.config.ssl_context,
        ) as _httpx_async:

            try:

                response = await _httpx_async.post(
                    f"{url}",  # required to turn pydantic object to str
                    json=payload.model_dump() if payload else None,
                    headers=self._get_authorization_headers(),
                )

                await _httpx_async.aclose()

                if response.status_code == HTTPStatus.OK:

                    if not response_class:
                        # TODO: should this return a boolean?
                        """No response to parse"""
                        return True

                    parsed_obj = response_class.model_validate(
                        response.json()
                    )

                    return parsed_obj

                elif response.status_code == HTTPStatus.FORBIDDEN:
                    raise UnlicensedFeatureException()
                elif response.status_code == HTTPStatus.UNAUTHORIZED:
                    raise AuthenticationError()

            except httpx.RequestError as e:
                raise (e)
