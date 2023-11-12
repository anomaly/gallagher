"""

"""

from ..utils import (
    APIBase,
    EndpointConfig
)

from ...dto.schedule import (
    ScheduleSummaryResponse
)


class Schedule(APIBase):
    """ Schedules
    """

    __config__ = EndpointConfig(
        endpoint="schedules",
        dto_list=ScheduleSummaryResponse,
    )
