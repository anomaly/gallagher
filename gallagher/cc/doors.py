from gallagher.cc.core import Capabilities, APIEndpoint, EndpointConfig

from ..dto.detail import DoorDetail
from ..dto.response import DoorResponse


class Doors(APIEndpoint):
    """Doors

    Provides access to door operations including listing,
    retrieving, creating, and updating doors.
    """

    @classmethod
    async def get_config(cls) -> EndpointConfig:
        return EndpointConfig(
            endpoint=Capabilities.CURRENT.features.doors.doors,
            dto_list=DoorResponse,
            dto_retrieve=DoorDetail,
        )
