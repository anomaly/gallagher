""" Door Summary

"""

from typing import Optional
from datetime import datetime

from ..utils import AppBaseModel, IdentityMixin, HrefMixin
from ..ref import DivisionRef


class DoorSummary(
    AppBaseModel,
    IdentityMixin,
    HrefMixin
):
    """Door Summary

    A summary view of a door containing key information
    for listing and basic operations.
    """

    name: str
    description: Optional[str] = None
    division: Optional[DivisionRef] = None
    status: Optional[str] = None
    created: Optional[datetime] = None
    modified: Optional[datetime] = None
