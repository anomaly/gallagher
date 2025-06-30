""" Visitor Detail

"""

from typing import Optional, List
from datetime import datetime

from ..utils import AppBaseModel, IdentityMixin, HrefMixin
from ..ref import DivisionRef, AccessGroupRef
from ..summary import VisitorSummary


class VisitorDetail(VisitorSummary):
    """Visitor Detail

    A detailed view of a visitor containing all information
    for comprehensive operations and management.
    """

    # Extended fields beyond summary
    access_groups: Optional[List[AccessGroupRef]] = None
    company: Optional[str] = None
    address: Optional[str] = None
    id_number: Optional[str] = None
    emergency_contact: Optional[str] = None
    emergency_phone: Optional[str] = None
    notes: Optional[str] = None
    photo_url: Optional[str] = None
