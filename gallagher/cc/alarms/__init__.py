""" Alarms


"""

from ..core import (
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

    @classmethod
    def get_config(cls):
        return EndpointConfig(
            endpoint=cls._capabilities.features.alarms.alarms.href,
            dto_list=AlarmResponse,
            dto_retrieve=AlarmZoneSummary,
        )
