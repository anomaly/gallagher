""" Zone Response

"""

from typing import List

from ..utils import AppBaseResponseWithFollowModel
from ..summary import ZoneSummary


class ZoneResponse(AppBaseResponseWithFollowModel):
    """Zone Response

    A response containing a list of zones with pagination support.
    """

    results: List[ZoneSummary]
