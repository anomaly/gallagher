from ..utils import (
    AppBaseResponseModel,
    HrefMixin,
)

from ..summary import (
    AlarmZoneSummary,
)


class AlarmSummaryResponse(
    AppBaseResponseModel,
):
    """ AlarmSummaryResponse represents a single alarm
    """
    alarms: list[AlarmZoneSummary]
    updates: HrefMixin
