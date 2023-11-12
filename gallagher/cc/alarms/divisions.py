"""

"""

from ..utils import (
    APIBase,
    EndpointConfig
)


class Division(APIBase):
    """
    Gallagher advises against hardcoding the URLs for divisions, and instead
    recommends using the /api endpoint to discover the URLs from 
    events.divisions.href and alarms.division.href.

    """

    __config__ = EndpointConfig(
        endpoint="divisions",
    )
