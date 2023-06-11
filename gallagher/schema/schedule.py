""" Schedules

"""

from .utils import AppBaseModel, HrefMixin

class ScheduleRef(
    AppBaseModel,
    HrefMixin
):
    """ Schedule is a time
    """
    pass


class ScheduleSummary(
    ScheduleRef
):
    """ Schedule is a time
    """
    name: str


class ScheduleSummaryResponse(
    AppBaseModel
):
    """ Schedule is a time
    """
    results: list[ScheduleSummary]
