""" Interlock Group Response

"""

from typing import List

from ..utils import AppBaseResponseWithFollowModel
from ..summary.interlock_group import InterlockGroupSummary


class InterlockGroupResponse(AppBaseResponseWithFollowModel):
    """Interlock Group Response

    A response containing a list of interlock groups with pagination support.
    """

    results: List[InterlockGroupSummary]
