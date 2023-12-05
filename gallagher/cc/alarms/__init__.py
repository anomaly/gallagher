""" Alarms


"""

from ..core import (
    APIEndpoint,
    EndpointConfig,
    Capabilities
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

    @classmethod
    def get_config(cls):
        return EndpointConfig(
            endpoint=Capabilities.CURRENT.features.alarms.alarms.href,
            dto_list=AlarmResponse,
            dto_retrieve=AlarmZoneSummary,
        )
