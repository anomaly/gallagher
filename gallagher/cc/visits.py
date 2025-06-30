""" Visits

"""

from .core import Capabilities, APIEndpoint, EndpointConfig
from ..dto.detail import VisitDetail
from ..dto.response import VisitResponse


class Visits(APIEndpoint):
    """Visits
    Provides access to visit operations including listing, retrieving, creating, and updating visits.
    """
    @classmethod
    async def get_config(cls) -> EndpointConfig:
        return EndpointConfig(
            endpoint=Capabilities.CURRENT.features.visits.visits,
            dto_list=VisitResponse,
            dto_retrieve=VisitDetail,
        )
