""" Day Category Detail

"""

from typing import Optional, List
from datetime import datetime

from ..utils import AppBaseModel, IdentityMixin, HrefMixin
from ..ref import DivisionRef
from ..summary import DayCategorySummary


class DayCategoryDetail(DayCategorySummary):
    """Day Category Detail

    A detailed view of a day category containing all information
    for comprehensive operations and management.
    """

    # Extended fields beyond summary
    time_periods: Optional[List[dict]] = None
    exceptions: Optional[List[dict]] = None
    notes: Optional[str] = None
    is_default: Optional[bool] = None
