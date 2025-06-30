""" Role Summary

"""

from typing import Optional
from datetime import datetime

from ..utils import AppBaseModel, IdentityMixin, HrefMixin
from ..ref import DivisionRef


class RoleSummary(
    AppBaseModel,
    IdentityMixin,
    HrefMixin
):
    """Role Summary

    A summary view of a role containing key information
    for listing and basic operations.
    """

    name: str
    description: Optional[str] = None
    division: Optional[DivisionRef] = None
    active: Optional[bool] = None
    created: Optional[datetime] = None
    modified: Optional[datetime] = None
