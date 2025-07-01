""" Receptions

"""

from gallagher.cc.core import Capabilities, APIEndpoint, EndpointConfig

from ..dto.detail import ReceptionDetail
from ..dto.response import ReceptionResponse


class Receptions(APIEndpoint):
    """Receptions

    Provides access to reception operations including listing,
    retrieving, creating, and updating receptions.
    """

    @classmethod
    async def get_config(cls) -> EndpointConfig:
        return EndpointConfig(
            endpoint=Capabilities.CURRENT.features.receptions.receptions,
            dto_list=ReceptionResponse,
            dto_retrieve=ReceptionDetail,
        )
