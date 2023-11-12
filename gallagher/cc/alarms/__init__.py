"""


"""

from ..utils import (
    APIBase,
    EndpointConfig
)

from ...dto.alarm import (
    AlarmResponse,
    AlarmZoneSummary
)


class Alarms(
    APIBase
):
    """ Alarms
    """

    __config__ = EndpointConfig(
        endpoint="alarms",
        dto_list=AlarmResponse,
        dto_retrieve=AlarmZoneSummary,
    )
