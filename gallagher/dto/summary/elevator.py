""" Elevator Group Summary

"""

from typing import Optional

from ..utils import AppBaseModel, IdentityMixin, HrefMixin
from ..ref import DivisionRef


class ElevatorSummary(
    AppBaseModel,
    IdentityMixin,
    HrefMixin,
):
    """Elevator Group Summary

    A summary view of an elevator group containing key information
    for listing and basic operations.
    """

    name: str
    description: Optional[str] = None
    division: Optional[DivisionRef] = None
    server_display_name: Optional[str] = None
