""" Locker Response

"""

from typing import List

from ..utils import AppBaseResponseWithFollowModel
from ..summary import LockerSummary


class LockerResponse(AppBaseResponseWithFollowModel):
    """Locker Response

    A response containing a list of lockers with pagination support.
    """

    results: List[LockerSummary]
