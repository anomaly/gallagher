""" Visit Summary

"""

from typing import Optional
from datetime import datetime

from ..utils import AppBaseModel, IdentityMixin, HrefMixin
from ..ref import VisitorRef, CardholderRef


class VisitSummary(
    AppBaseModel,
    IdentityMixin,
    HrefMixin
):
    """Visit Summary

    A summary view of a visit containing key information
    for listing and basic operations.
    """

    visitor: Optional[VisitorRef] = None
    host: Optional[CardholderRef] = None
    visit_date: Optional[datetime] = None
    status: Optional[str] = None
    created: Optional[datetime] = None
    modified: Optional[datetime] = None
