from gallagher.cc.core import APIEndpoint, EndpointConfig

from ..dto.detail import DoorDetail
from ..dto.response import DoorResponse


class Door(APIEndpoint):
    """Doors

    Provides access to door operations including listing,
    retrieving, creating, and updating doors.
    """

    def get_config(self) -> EndpointConfig:
        return EndpointConfig(
            endpoint=self._CAPABILITIES.features.doors.doors,
            dto_list=DoorResponse,
            dto_retrieve=DoorDetail,
        )
