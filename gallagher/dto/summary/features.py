""" Features Summary

"""

from typing import Optional
from datetime import datetime

from ..utils import AppBaseModel, IdentityMixin, HrefMixin


class FeaturesSummary(
    AppBaseModel,
    IdentityMixin,
    HrefMixin
):
    """Features Summary

    A summary view of features containing key information
    for listing and basic operations.
    """

    name: str
    description: Optional[str] = None
    version: Optional[str] = None
    created: Optional[datetime] = None
    modified: Optional[datetime] = None
