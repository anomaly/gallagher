"""

"""

from ..core import (
    Capabilities,
    APIEndpoint,
    EndpointConfig
)

from ...dto.detail import (
    DivisionDetail,
)

from ...dto.response import (
    DivisionDetailResponse,
)


class Division(APIEndpoint):
    """
    Gallagher advises against hardcoding the URLs for divisions, and instead
    recommends using the /api endpoint to discover the URLs from 
    events.divisions.href and alarms.division.href.

    """

    @classmethod
    async def get_config(cls) -> EndpointConfig:
        return EndpointConfig(
            endpoint=Capabilities.CURRENT.features.divisions.divisions,
            dto_list=DivisionDetailResponse,
            dto_retrieve=DivisionDetail,
        )
