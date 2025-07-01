""" Features Detail

"""

from typing import Optional, List
from datetime import datetime

from ..utils import AppBaseModel, IdentityMixin, HrefMixin
from ..summary import FeaturesSummary


class FeaturesDetail(FeaturesSummary):
    """Features Detail

    A detailed view of features containing all information
    for comprehensive operations and management.
    """

    # Extended fields beyond summary
    available_features: Optional[List[str]] = None
    licensed_features: Optional[List[str]] = None
    configuration: Optional[dict] = None
    notes: Optional[str] = None
