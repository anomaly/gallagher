""" Door Response

"""

from typing import List

from ..utils import AppBaseResponseWithFollowModel
from ..summary import DoorSummary


class DoorResponse(AppBaseResponseWithFollowModel):
    """Door Response

    A response containing a list of doors with pagination support.
    """

    results: List[DoorSummary]


DoorSummaryResponse = DoorResponse
