""" Locker Detail

"""

from typing import Optional, List
from datetime import datetime

from ..utils import AppBaseModel, IdentityMixin, HrefMixin
from ..ref import DivisionRef, CardholderRef
from ..summary import LockerSummary


class LockerDetail(LockerSummary):
    """Locker Detail

    A detailed view of a locker containing all information
    for comprehensive operations and management.
    """

    # Extended fields beyond summary
    assigned_cardholder: Optional[CardholderRef] = None
    locker_type: Optional[str] = None
    status_details: Optional[str] = None
    location: Optional[str] = None
    notes: Optional[str] = None
    last_accessed: Optional[datetime] = None
