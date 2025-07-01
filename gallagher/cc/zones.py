""" Zones

"""

from gallagher.cc.core import Capabilities, APIEndpoint, EndpointConfig

from ..dto.detail import ZoneDetail
from ..dto.response import ZoneResponse


class Zones(APIEndpoint):
    """Zones

    Provides access to zone operations including listing,
    retrieving, creating, and updating zones.
    """

    @classmethod
    async def get_config(cls) -> EndpointConfig:
        return EndpointConfig(
            endpoint=Capabilities.CURRENT.features.access_zones.access_zones,
            dto_list=ZoneResponse,
            dto_retrieve=ZoneDetail,
        )
