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

    CLOUD_GATEWAY_AU = ["3.106.1.6", "3.106.100.112"]

    CLOUD_GATEWAY_US = ["44.193.42.111", "3.209.194.103"]
