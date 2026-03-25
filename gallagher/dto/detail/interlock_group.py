""" Interlock Group Detail

"""

from typing import Optional, List

from ..ref import DoorRef
from ..summary.interlock_group import InterlockGroupSummary


class InterlockGroupDetail(InterlockGroupSummary):
    """Interlock Group Detail

    A detailed view of an interlock group containing all information
    for comprehensive operations and management.
    """

    interlock_type: Optional[str] = None
    notes: Optional[str] = None
    doors: Optional[List[DoorRef]] = None
