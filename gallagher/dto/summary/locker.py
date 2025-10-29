""" Locker Summary

"""

from typing import Optional
from datetime import datetime

from ..utils import AppBaseModel, IdentityMixin, HrefMixin
from ..ref import DivisionRef


class LockerSummary(
    AppBaseModel,
    IdentityMixin,
    HrefMixin
):
    """Locker Summary

    A summary view of a locker containing key information
    for listing and basic operations.
    """

    id: Optional[str] = None
    name: str
    description: Optional[str] = None
    division: Optional[DivisionRef] = None
    bank_id: str
    status: Optional[str] = None
    created: Optional[datetime] = None
    modified: Optional[datetime] = None
