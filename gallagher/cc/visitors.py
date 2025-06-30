""" Visitors

"""

from ..core import Capabilities, APIEndpoint, EndpointConfig

from ..dto.detail import VisitorDetail
from ..dto.response import VisitorResponse


class Visitors(APIEndpoint):
    """Visitors

    Provides access to visitor operations including listing,
    retrieving, creating, and updating visitors.
    """

    @classmethod
    async def get_config(cls) -> EndpointConfig:
        return EndpointConfig(
            endpoint=Capabilities.CURRENT.features.visitors.visitors,
            dto_list=VisitorResponse,
            dto_retrieve=VisitorDetail,
        )
