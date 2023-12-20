from ..utils import (
    AppBaseModel,
)

from ..summary import (
    ScheduleSummary
)


class ScheduleSummaryResponse(
    AppBaseModel
):
    """ Schedule is a time
    """
    results: list[ScheduleSummary]
