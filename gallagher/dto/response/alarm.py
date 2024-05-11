from ..utils import (
    AppBaseResponseModel,
    HrefMixin,
)

from ..summary import (
    AlarmSummary,
)


class AlarmSummaryResponse(
    AppBaseResponseModel,
):
    """AlarmSummaryResponse represents a single alarm"""

    alarms: list[AlarmSummary]
    updates: HrefMixin
