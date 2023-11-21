"""


"""

from ..utils import (
    APIEndpoint,
    EndpointConfig
)

from ...dto.alarm import (
    AlarmResponse,
    AlarmZoneSummary
)


class Alarms(
    APIEndpoint
):
    """ Alarms
    """

    __config__ = EndpointConfig(
        endpoint="alarms",
        dto_list=AlarmResponse,
        dto_retrieve=AlarmZoneSummary,
    )
