""" Zone Summary

"""

from typing import Optional
from datetime import datetime

from ..utils import AppBaseModel, IdentityMixin, HrefMixin
from ..ref import DivisionRef


class ZoneSummary(
    AppBaseModel,
    IdentityMixin,
    HrefMixin
):
    """Zone Summary

    A summary view of a zone containing key information
    for listing and basic operations.
    """

    name: str
    description: Optional[str] = None
    division: Optional[DivisionRef] = None
    zone_type: Optional[str] = None
    created: Optional[datetime] = None
    modified: Optional[datetime] = None
