from gallagher.dto.utils import (
    AppBaseModel,
)

from ..ref import (
    ScheduleSummary
)


class ScheduleSummaryResponse(
    AppBaseModel
):
    """ Schedule is a time
    """
    results: list[ScheduleSummary]
