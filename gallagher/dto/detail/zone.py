""" Zone Detail

"""

from typing import Optional, List
from datetime import datetime

from ..utils import AppBaseModel, IdentityMixin, HrefMixin
from ..ref import DivisionRef, DoorRef
from ..summary import ZoneSummary


class ZoneDetail(ZoneSummary):
    """Zone Detail

    A detailed view of a zone containing all information
    for comprehensive operations and management.
    """

    # Extended fields beyond summary
    doors: Optional[List[DoorRef]] = None
    zone_boundaries: Optional[List[dict]] = None
    access_rules: Optional[List[dict]] = None
    notes: Optional[str] = None
    security_level: Optional[str] = None
