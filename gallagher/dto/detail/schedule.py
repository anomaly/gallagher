""" Schedule Detail

"""

from typing import Optional, List
from datetime import datetime

from ..utils import AppBaseModel, IdentityMixin, HrefMixin
from ..ref import DivisionRef, DayCategoryRef
from ..summary import ScheduleSummary


class ScheduleDetail(ScheduleSummary):
    """Schedule Detail

    A detailed view of a schedule containing all information
    for comprehensive operations and management.
    """

    # Extended fields beyond summary
    day_categories: Optional[List[DayCategoryRef]] = None
    time_periods: Optional[List[dict]] = None
    exceptions: Optional[List[dict]] = None
    notes: Optional[str] = None
    is_default: Optional[bool] = None
