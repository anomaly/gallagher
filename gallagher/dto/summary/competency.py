""" Competency Summary

"""

from typing import Optional

from ..utils import AppBaseModel, IdentityMixin, HrefMixin
from ..ref import DivisionRef


class CompetencySummary(
    AppBaseModel,
    IdentityMixin,
    HrefMixin,
):
    """Competency Summary

    A summary view of a competency containing key information
    for listing and basic operations.
    """

    name: str
    description: Optional[str] = None
    division: Optional[DivisionRef] = None
