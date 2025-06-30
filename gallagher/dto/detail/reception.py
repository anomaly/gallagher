""" Reception Detail

"""

from typing import Optional, List
from datetime import datetime

from ..utils import AppBaseModel, IdentityMixin, HrefMixin
from ..ref import DivisionRef, CardholderRef
from ..summary import ReceptionSummary


class ReceptionDetail(ReceptionSummary):
    """Reception Detail

    A detailed view of a reception containing all information
    for comprehensive operations and management.
    """

    # Extended fields beyond summary
    receptionist: Optional[CardholderRef] = None
    location: Optional[str] = None
    contact_info: Optional[str] = None
    operating_hours: Optional[str] = None
    notes: Optional[str] = None
    visitor_check_in_process: Optional[str] = None
