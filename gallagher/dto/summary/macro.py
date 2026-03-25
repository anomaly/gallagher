""" Macro Summary

"""

from typing import Optional

from ..utils import AppBaseModel, IdentityMixin, HrefMixin
from ..ref import DivisionRef


class MacroSummary(
    AppBaseModel,
    IdentityMixin,
    HrefMixin,
):
    """Macro Summary

    A summary view of a macro containing key information
    for listing and basic operations.
    """

    name: str
    description: Optional[str] = None
    division: Optional[DivisionRef] = None
