"""

"""

from ..utils import APIBase
from ...dto.schedule import ScheduleSummaryResponse


class Schedule(APIBase):
    """ Schedules
    """

    class Config:

        endpoint = "schedules"
        list_response_class = ScheduleSummaryResponse
