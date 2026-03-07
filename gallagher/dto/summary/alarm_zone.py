""" Alarm Zone Summary

"""

from typing import Optional

from ..utils import AppBaseModel, IdentityMixin, HrefMixin
from ..ref import DivisionRef


class AlarmZoneSummary(
    AppBaseModel,
    IdentityMixin,
    HrefMixin,
):
    """Alarm Zone Summary

    A summary view of an alarm zone containing key information
    for listing and basic operations.
    """

    name: str
    description: Optional[str] = None
    division: Optional[DivisionRef] = None
    server_display_name: Optional[str] = None
