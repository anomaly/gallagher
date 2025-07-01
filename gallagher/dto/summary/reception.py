""" Reception Summary

"""

from typing import Optional
from datetime import datetime

from ..utils import AppBaseModel, IdentityMixin, HrefMixin
from ..ref import DivisionRef


class ReceptionSummary(
    AppBaseModel,
    IdentityMixin,
    HrefMixin
):
    """Reception Summary

    A summary view of a reception containing key information
    for listing and basic operations.
    """

    id: Optional[str] = None
    name: str
    description: Optional[str] = None
    division: Optional[DivisionRef] = None
    active: Optional[bool] = None
    created: Optional[datetime] = None
    modified: Optional[datetime] = None
