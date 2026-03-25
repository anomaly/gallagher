""" Zones

"""

from gallagher.cc.core import APIEndpoint, EndpointConfig

from ..dto.detail import ZoneDetail
from ..dto.response import ZoneResponse


class Zone(APIEndpoint):
    """Zones

    Provides access to zone operations including listing,
    retrieving, creating, and updating zones.
    """

    def get_config(self) -> EndpointConfig:
        return EndpointConfig(
            endpoint=self._CAPABILITIES.features.access_zones.access_zones,
            dto_list=ZoneResponse,
            dto_retrieve=ZoneDetail,
        )
