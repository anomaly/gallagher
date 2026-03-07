""" Fence Zone Response

"""

from typing import List

from ..utils import AppBaseResponseWithFollowModel
from ..summary.fence_zone import FenceZoneSummary


class FenceZoneResponse(AppBaseResponseWithFollowModel):
    """Fence Zone Response

    A response containing a list of fence zones with pagination support.
    """

    results: List[FenceZoneSummary]
