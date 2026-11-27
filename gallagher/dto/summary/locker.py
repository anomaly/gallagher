""" Locker Summary

"""

from typing import Optional
from datetime import datetime

from ..utils import AppBaseModel, OptionalIdentityMixin, HrefMixin
from ..ref import DivisionRef


class LockerSummary(
    AppBaseModel,
    OptionalIdentityMixin,
    HrefMixin
):
    """Locker Summary

    A summary view of a locker containing key information
    for listing and basic operations.
    """

    name: str
    description: Optional[str] = None
    division: Optional[DivisionRef] = None
    bank_id: str
    status: Optional[str] = None
    created: Optional[datetime] = None
    modified: Optional[datetime] = None
