from ..utils import (
    AppBaseResponseModel,
)

from ..summary import ScheduleSummary


class ScheduleSummaryResponse(
    AppBaseResponseModel,
):
    """Schedule is a time"""

    results: list[ScheduleSummary]
