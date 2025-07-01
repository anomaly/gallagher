""" Features Response

"""

from typing import List

from ..utils import AppBaseResponseWithFollowModel
from ..summary import FeaturesSummary


class FeaturesResponse(AppBaseResponseWithFollowModel):
    """Features Response

    A response containing a list of features with pagination support.
    """

    results: List[FeaturesSummary]
