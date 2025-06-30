""" Operators

"""

from ..core import Capabilities, APIEndpoint, EndpointConfig

from ..dto.detail import OperatorDetail
from ..dto.response import OperatorResponse


class Operators(APIEndpoint):
    """Operators

    Provides access to operator operations including listing,
    retrieving, creating, and updating operators.
    """

    @classmethod
    async def get_config(cls) -> EndpointConfig:
        return EndpointConfig(
            endpoint=Capabilities.CURRENT.features.operator_groups.operator_groups,
            dto_list=OperatorResponse,
            dto_retrieve=OperatorDetail,
        )
