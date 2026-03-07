""" Elevator Group Detail

"""

from typing import Optional, List

from ..utils import OptionalHrefMixin
from ..ref import DoorRef
from ..summary.elevator import ElevatorSummary


class ElevatorDetail(ElevatorSummary):
    """Elevator Group Detail

    A detailed view of an elevator group containing all information
    for comprehensive operations and management.
    """

    doors: Optional[List[DoorRef]] = None
    floors: Optional[List[dict]] = None
    notes: Optional[str] = None
