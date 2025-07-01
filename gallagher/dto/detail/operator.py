""" Operator Detail

"""

from typing import Optional, List
from datetime import datetime

from ..utils import AppBaseModel, IdentityMixin, HrefMixin
from ..ref import DivisionRef, RoleRef
from ..summary import OperatorSummary


class OperatorDetail(OperatorSummary):
    """Operator Detail

    A detailed view of an operator containing all information
    for comprehensive operations and management.
    """

    # Extended fields beyond summary
    roles: Optional[List[RoleRef]] = None
    permissions: Optional[List[str]] = None
    login_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    notes: Optional[str] = None
    last_login: Optional[datetime] = None
