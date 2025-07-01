""" Access Group Response

"""

from typing import List

from ..utils import AppBaseResponseWithFollowModel
from ..summary import AccessGroupSummary


class AccessGroupResponse(AppBaseResponseWithFollowModel):
    """Access Group Response

    A response containing a list of access groups with pagination support.
    """

    results: List[AccessGroupSummary]
