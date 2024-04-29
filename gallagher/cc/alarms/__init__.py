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
    AlarmSummaryResponse,
)


class Alarms(
    APIEndpoint
):
    """ Alarms
    """

    @classmethod
    async def get_config(cls) -> EndpointConfig:
        return EndpointConfig(
            endpoint=Capabilities.CURRENT.features.alarms.alarms,
            dto_list=AlarmSummaryResponse,
            dto_retrieve=AlarmZoneSummary,
        )
