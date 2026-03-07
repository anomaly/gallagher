""" Interlock Group Summary

"""

from typing import Optional

from ..utils import AppBaseModel, IdentityMixin, HrefMixin
from ..ref import DivisionRef


class InterlockGroupSummary(
    AppBaseModel,
    IdentityMixin,
    HrefMixin,
):
    """Interlock Group Summary

    A summary view of an interlock group containing key information
    for listing and basic operations.
    """

    name: str
    description: Optional[str] = None
    division: Optional[DivisionRef] = None
