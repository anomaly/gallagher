""" Door Detail

"""

from typing import Optional, List
from datetime import datetime

from ..utils import AppBaseModel, IdentityMixin, HrefMixin
from ..ref import DivisionRef, AccessGroupRef, ScheduleRef
from ..summary import DoorSummary


class DoorDetail(DoorSummary):
    """Door Detail

    A detailed view of a door containing all information
    for comprehensive operations and management.
    """

    # Extended fields beyond summary
    door_type: Optional[str] = None
    access_groups: Optional[List[AccessGroupRef]] = None
    schedule: Optional[ScheduleRef] = None
    status_details: Optional[str] = None
    hardware_info: Optional[dict] = None
    location: Optional[str] = None
    notes: Optional[str] = None
