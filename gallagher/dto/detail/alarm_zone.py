""" Alarm Zone Detail

"""

from typing import Optional, List

from ..utils import AppBaseModel, HrefMixin, OptionalHrefMixin
from ..ref import DivisionRef, AccessZoneRef
from ..summary.alarm_zone import AlarmZoneSummary


class AlarmZoneDetail(AlarmZoneSummary):
    """Alarm Zone Detail

    A detailed view of an alarm zone containing all information
    for comprehensive operations and management.
    """

    armed: Optional[bool] = None
    cardholder_count: Optional[int] = None
    access_zones: Optional[List[AccessZoneRef]] = None
    arm: OptionalHrefMixin = None
    disarm: OptionalHrefMixin = None
