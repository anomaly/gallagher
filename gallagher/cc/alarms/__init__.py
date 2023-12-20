""" Alarms


"""

from ..core import (
    APIEndpoint,
    EndpointConfig,
    Capabilities
)

from ...dto.summary import (
    AlarmZoneSummary
)

from ...dto.response import (
    AlarmResponse,
)


class Alarms(
    APIEndpoint
):
    """ Alarms
    """

    @classmethod
    async def get_config(cls):
        return EndpointConfig(
            endpoint=Capabilities.CURRENT.features.alarms.alarms,
            dto_list=AlarmResponse,
            dto_retrieve=AlarmZoneSummary,
        )
