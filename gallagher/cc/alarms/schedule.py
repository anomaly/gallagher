"""

"""

from ..core import APIEndpoint, EndpointConfig

from ...dto.response import ScheduleSummaryResponse


class Schedule(APIEndpoint):
    """Schedules"""

    def get_config(self) -> EndpointConfig:
        return EndpointConfig(
            endpoint=self._CAPABILITIES.features.schedules.schedules,
            dto_list=ScheduleSummaryResponse,
        )
