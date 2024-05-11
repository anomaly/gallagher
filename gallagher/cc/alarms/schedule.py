"""

"""

from ..core import Capabilities, APIEndpoint, EndpointConfig

from ...dto.response import ScheduleSummaryResponse


class Schedule(APIEndpoint):
    """Schedules"""

    @classmethod
    async def get_config(cls) -> EndpointConfig:
        return EndpointConfig(
            endpoint=Capabilities.CURRENT.features.schedules.schedules,
            dto_list=ScheduleSummaryResponse,
        )
