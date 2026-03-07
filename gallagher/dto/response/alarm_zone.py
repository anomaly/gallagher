""" Alarm Zone Response

"""

from typing import List

from ..utils import AppBaseResponseWithFollowModel
from ..summary.alarm_zone import AlarmZoneSummary


class AlarmZoneResponse(AppBaseResponseWithFollowModel):
    """Alarm Zone Response

    A response containing a list of alarm zones with pagination support.
    """

    results: List[AlarmZoneSummary]
