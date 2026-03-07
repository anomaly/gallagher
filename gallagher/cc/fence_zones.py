""" Fence Zones

"""

from gallagher.cc.core import APIEndpoint, EndpointConfig

from ..dto.detail import FenceZoneDetail
from ..dto.response import FenceZoneResponse


class FenceZone(APIEndpoint):
    """Fence Zones

    Provides access to fence zone operations including listing
    and retrieving fence zones. Fence zones define virtual
    perimeter boundaries monitored by the command centre.
    """

    def get_config(self) -> EndpointConfig:
        return EndpointConfig(
            endpoint=self._CAPABILITIES.features.fence_zones.fence_zones,
            dto_list=FenceZoneResponse,
            dto_retrieve=FenceZoneDetail,
        )
