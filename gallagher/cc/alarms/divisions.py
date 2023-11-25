"""

"""

from ..core import (
    APIEndpoint,
    EndpointConfig
)

from ...dto.division import (
    DivisionDetailResponse,
    DivisionDetail,
)


class Division(APIEndpoint):
    """
    Gallagher advises against hardcoding the URLs for divisions, and instead
    recommends using the /api endpoint to discover the URLs from 
    events.divisions.href and alarms.division.href.

    """

    __config__ = EndpointConfig(
        endpoint="divisions",
        dto_list=DivisionDetailResponse,
        dto_retrieve=DivisionDetail,
    )
