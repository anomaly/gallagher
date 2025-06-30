""" Salto Detail

"""

from typing import Optional, List
from datetime import datetime

from ..utils import AppBaseModel, IdentityMixin, HrefMixin
from ..ref import DivisionRef
from ..summary import SaltoSummary


class SaltoDetail(SaltoSummary):
    """Salto Detail

    A detailed view of a Salto device containing all information
    for comprehensive operations and management.
    """

    # Extended fields beyond summary
    device_type: Optional[str] = None
    firmware_version: Optional[str] = None
    battery_level: Optional[int] = None
    last_sync: Optional[datetime] = None
    location: Optional[str] = None
    notes: Optional[str] = None
    hardware_info: Optional[dict] = None
