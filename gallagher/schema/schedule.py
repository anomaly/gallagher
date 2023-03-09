""" Schedules

"""

from .utils import AppBaseModel, HrefMixin

class ScheduleRef(
    AppBaseModel,
    HrefMixin
):
    """ Schedule is a time
    """
    name: str