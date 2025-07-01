""" Visit Response

"""

from typing import List

from ..utils import AppBaseResponseWithFollowModel
from ..summary import VisitSummary


class VisitResponse(AppBaseResponseWithFollowModel):
    """Visit Response

    A response containing a list of visits with pagination support.
    """

    results: List[VisitSummary]
