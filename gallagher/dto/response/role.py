""" Role Response

"""

from typing import List

from ..utils import AppBaseResponseWithFollowModel
from ..summary import RoleSummary


class RoleResponse(AppBaseResponseWithFollowModel):
    """Role Response

    A response containing a list of roles with pagination support.
    """

    results: List[RoleSummary]
