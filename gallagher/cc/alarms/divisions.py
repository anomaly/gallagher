""" Division

"""

from ..core import APIEndpoint, EndpointConfig

from ...dto.detail import (
    DivisionDetail,
)

from ...dto.response import (
    DivisionSummaryResponse,
)


class Division(APIEndpoint):
    """
    Gallagher advises against hardcoding the URLs for divisions, and instead
    recommends using the /api endpoint to discover the URLs from
    events.divisions.href and alarms.division.href.

    """

    def get_config(self) -> EndpointConfig:
        return EndpointConfig(
            endpoint=self._CAPABILITIES.features.divisions.divisions,
            dto_list=DivisionSummaryResponse,
            dto_retrieve=DivisionDetail,
        )
