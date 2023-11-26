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
from dataclasses import dataclass

import httpx

from gallagher.exception import (
    UnlicensedFeatureException
)

from ..dto.discover import (
    DiscoveryResponse,
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
    def validate_endpoint(cls):
        """ Check to see if the feature is licensed and available

        Gallagher REST API is licensed per feature, if a feature is not
        the endpoint is set to none and we should throw an exception
        """
        if not cls.endpoint:
            raise UnlicensedFeatureException(
                "Endpoint not defined"
            )


class APIEndpoint():
    """ Base class for all API objects

    All API endpoints must inherit from this class and provide a Config class
    that automates the implementation of many of the API methods.

    If the endpoints provide additional methods then they are to implement them
    based on the same standards as this base class.

    """

    # This must be overridden by each child class that inherits
    # from this base class.
    __config__ = None

    @classmethod
    def _discover(cls):
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
        """

        # Auto-discovery of the API endpoints, this will
        # be called as part of the bootstrapping process
        from . import api_base
        response = httpx.get(
            api_base,
            headers=get_authorization_headers(),
        )

        parsed_obj = DiscoveryResponse.model_validate(
            response.json()
        )

        from . import CAPABILITIES
        CAPABILITIES = parsed_obj

    @classmethod
    def list(cls, skip=0):
        """ For a list of objects for the given resource

        Most resources can be searched which is exposed by this method.
        Resources also allow pagination which can be controlled by the skip
        """
        cls._discover()

        from . import api_base
        response = httpx.get(
            f'{api_base}{cls.__config__.endpoint}',
            headers=get_authorization_headers(),
        )

        parsed_obj = cls.__config__.dto_list.model_validate(
            response.json()
        )

        return parsed_obj

    @classmethod
    def retrieve(cls, id):
        """ Retrieve a single object for the given resource

        Most objects have an ID which is numeral or UUID. 
        Each resource also provides a href and pagination for
        children.
        """
        cls._discover()

        from . import api_base
        response = httpx.get(
            f'{api_base}{cls.__config__.endpoint}/{id}',
            headers=get_authorization_headers(),
        )

        parsed_obj = cls.__config__.dto_retrieve.model_validate(
            response.json()
        )

        return parsed_obj

    @classmethod
    def modify(cls):
        """

        """
        pass

    @classmethod
    def create(cls, **params):
        """

        """
        pass

    @classmethod
    def delete(cls):
        """

        """
        pass

    @classmethod
    def search(cls, **kwargs):
        """ Search

        """
        pass

    @classmethod
    def updates(cls):
        pass
