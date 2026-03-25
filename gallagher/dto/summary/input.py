""" Input Summary

"""

from typing import Optional

from ..utils import AppBaseModel, IdentityMixin, HrefMixin
from ..ref import DivisionRef


class InputSummary(
    AppBaseModel,
    IdentityMixin,
    HrefMixin,
):
    """Input Summary

    A summary view of an input containing key information
    for listing and basic operations.
    """

    name: str
    description: Optional[str] = None
    division: Optional[DivisionRef] = None
    status: Optional[str] = None
