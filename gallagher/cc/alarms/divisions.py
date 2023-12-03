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

    @classmethod
    def get_config(cls):
        return EndpointConfig(
            endpoint=APIEndpoint._capabilities.features.divisions.divisions.href,
            dto_list=DivisionDetailResponse,
            dto_retrieve=DivisionDetail,
        )
