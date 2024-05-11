from ..utils import AppBaseModel, HrefMixin


class ScheduleSummary(AppBaseModel, HrefMixin):
    """Schedule is a time"""

    name: str
