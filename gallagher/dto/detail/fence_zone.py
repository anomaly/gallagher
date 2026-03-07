""" Fence Zone Detail

"""

from typing import Optional, List

from ..utils import OptionalHrefMixin
from ..summary.fence_zone import FenceZoneSummary


class FenceZoneDetail(FenceZoneSummary):
    """Fence Zone Detail

    A detailed view of a fence zone containing all information
    for comprehensive operations and management.
    """

    zone_type: Optional[str] = None
    notes: Optional[str] = None
    items: Optional[List[dict]] = None
    arm: OptionalHrefMixin = None
    disarm: OptionalHrefMixin = None
