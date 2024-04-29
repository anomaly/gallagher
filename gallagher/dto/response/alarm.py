from ..utils import (
    AppBaseResponseModel,
    HrefMixin,
)

from ..summary import (
    AlarmZoneSummary,
)


class AlarmResponse(
    AppBaseResponseModel,
):
    """ AlarmResponse represents a single alarm
    """
    alarms: list[AlarmZoneSummary]
    updates: HrefMixin
