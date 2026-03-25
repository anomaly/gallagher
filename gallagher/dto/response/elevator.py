""" Elevator Group Response

"""

from typing import List

from ..utils import AppBaseResponseWithFollowModel
from ..summary.elevator import ElevatorSummary


class ElevatorResponse(AppBaseResponseWithFollowModel):
    """Elevator Group Response

    A response containing a list of elevator groups with pagination support.
    """

    results: List[ElevatorSummary]
