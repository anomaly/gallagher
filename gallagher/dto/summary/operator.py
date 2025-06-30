""" Operator Summary

"""

from typing import Optional
from datetime import datetime

from ..utils import AppBaseModel, IdentityMixin, HrefMixin
from ..ref import DivisionRef


class OperatorSummary(
    AppBaseModel,
    IdentityMixin,
    HrefMixin
):
    """Operator Summary

    A summary view of an operator containing key information
    for listing and basic operations.
    """

    name: str
    description: Optional[str] = None
    division: Optional[DivisionRef] = None
    active: Optional[bool] = None
    created: Optional[datetime] = None
    modified: Optional[datetime] = None
