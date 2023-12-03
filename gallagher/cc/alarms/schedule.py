"""

"""

from ..core import (
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
            endpoint=cls._discover.features.schedules.schedules.href,
            dto_list=ScheduleSummaryResponse,
        )
