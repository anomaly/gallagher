""" Visitor Response

"""

from typing import List

from ..utils import AppBaseResponseWithFollowModel
from ..summary import VisitorSummary


class VisitorResponse(AppBaseResponseWithFollowModel):
    """Visitor Response

    A response containing a list of visitors with pagination support.
    """

    results: List[VisitorSummary]
