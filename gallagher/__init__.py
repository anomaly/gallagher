"""" Gallagher Python bindings

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

api_key: str = None
api_base: str = None
client_id: str = None
proxy: Optional[str] = None
