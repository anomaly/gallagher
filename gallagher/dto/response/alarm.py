from gallagher.dto.utils import (
    AppBaseModel,
    HrefMixin,
)

from ..summary import (
    AlarmZoneSummary,
)


class AlarmResponse(
    AppBaseModel,
):
    """ AlarmResponse represents a single alarm
    """
    alarms: list[AlarmZoneSummary]
    updates: HrefMixin
