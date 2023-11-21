""" Command Centre bindings

    After enabling the Gateway for your server and REST API user, you need 
    only to replace the local server's URL with the cloud API Gateway one.
    
    Example Local request:

            <client certificate thumbprint e89ef121958...>
            GET https://servername.yourcompany.local:8904/api/cardholders
            Authorization: GGL-API-KEY F6F0-C8F0-
        
    Equivalent Gateway request:

          <client certificate thumbprint e89ef121958...>
          GET https://commandcentre-api-au.security.gallagher.cloud/api/cardholders
          Authorization: GGL-API-KEY F6F0-C8F0-60AF-

    The API client takes of appending the headers onto the requests.


"""

from typing import Optional

from ..const import URL
from ..dto.discover import DiscoveryResponse

from .utils import (
    APIEndpoint,
    EndpointConfig
)

# Follow the instructions in the Gallagher documentation
# to obtain an API key
api_key: str = None

# By default the base API is set to the Australian Gateway
# Override this with the US gateway or a local DNS/IP address
api_base: str = URL.CLOUD_GATEWAY_AU

# Default is set to the library, set this to your application
client_id: str = "gallagher-py"

# By default connections are sent straight to the server
# should you wish to use a proxy, set this to the proxy URL
proxy: Optional[str] = None


class APIFeatureDiscovery(
    APIEndpoint
):
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
    __config__ = EndpointConfig(
        endpoint="",  # The root endpoint is the discovery endpoint
        dto_list=DiscoveryResponse,
    )
