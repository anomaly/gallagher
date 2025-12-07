"""

"""

from ..core import Capabilities, APIEndpoint, EndpointConfig

from ...dto.response import ScheduleSummaryResponse


class Schedule(APIEndpoint):
    """Schedules"""

    def get_config(self) -> EndpointConfig:
        return EndpointConfig(
            endpoint=Capabilities.CURRENT.features.schedules.schedules,
            dto_list=ScheduleSummaryResponse,
        )
