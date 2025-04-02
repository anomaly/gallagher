""" Constants for the Gallagher Cloud ecosystem 

Gallagher publishes a set of networking constants for their cloud gateways
these should be updated as the documentation is updated.
"""


class URL:
    """DNS names for the cloud gateways

    These are published by Gallagher on Github
    https://gallaghersecurity.github.io/commandcentre-cloud-api-gateway.html
    """

    CLOUD_GATEWAY_AU: str = "https://commandcentre-api-au.security.gallagher.cloud/api/"
    CLOUD_GATEWAY_US: str = "https://commandcentre-api-us.security.gallagher.cloud/api/"


class IP_ADDR:
    """IP addresses for the cloud gateways

    These are published by Gallagher on Github
    https://gallaghersecurity.github.io/commandcentre-cloud-api-gateway.html
    """

    CLOUD_GATEWAY_AU: list[str] = ["3.106.1.6", "3.106.100.112"]

    CLOUD_GATEWAY_US: list[str] = ["44.193.42.111", "3.209.194.103"]


class TRANSPORT:
    """ Constants for the transport layer

    These are at present used to configure the httpx client
    they are based on the documentation provided by Gallagher
    """

    TIMEOUT_POLL = 60.0 # seconds, CC says it should be around 30 seconds