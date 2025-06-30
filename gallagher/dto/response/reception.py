""" Reception Response

"""

from typing import List

from ..utils import AppBaseResponseWithFollowModel
from ..summary import ReceptionSummary


class ReceptionResponse(AppBaseResponseWithFollowModel):
    """Reception Response

    A response containing a list of receptions with pagination support.
    """

    results: List[ReceptionSummary]
