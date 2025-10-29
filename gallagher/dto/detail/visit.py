""" Visit Detail

"""

from typing import Optional, List
from datetime import datetime

from ..utils import AppBaseModel, IdentityMixin, HrefMixin
from ..ref import VisitorRef, CardholderRef, AccessGroupRef
from ..summary import VisitSummary


class VisitDetail(VisitSummary):
    """Visit Detail

    A detailed view of a visit containing all information
    for comprehensive operations and management.
    """

    # Extended fields beyond summary
    access_groups: Optional[List[AccessGroupRef]] = None
    visit_reason: Optional[str] = None
    expected_arrival: Optional[datetime] = None
    expected_departure: Optional[datetime] = None
    actual_arrival: Optional[datetime] = None
    actual_departure: Optional[datetime] = None
    notes: Optional[str] = None
    approved_by: Optional[CardholderRef] = None
