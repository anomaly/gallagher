""" Operator Response

"""

from typing import List

from ..utils import AppBaseResponseWithFollowModel
from ..summary import OperatorSummary


class OperatorResponse(AppBaseResponseWithFollowModel):
    """Operator Response

    A response containing a list of operators with pagination support.
    """
    results: List[OperatorSummary]
