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

    __config__ = EndpointConfig(
        endpoint="schedules",
        dto_list=ScheduleSummaryResponse,
    )
