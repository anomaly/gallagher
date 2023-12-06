"""

"""

from ..core import (
    Capabilities,
    APIEndpoint,
    EndpointConfig
)

from ...dto.schedule import (
    ScheduleSummaryResponse
)


class Schedule(APIEndpoint):
    """ Schedules
    """

    @classmethod
    def get_config(cls):
        return EndpointConfig(
            endpoint=Capabilities.CURRENT.features.schedules.schedules,
            dto_list=ScheduleSummaryResponse,
        )
