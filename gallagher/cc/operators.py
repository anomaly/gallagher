""" Operators

"""

from gallagher.cc.core import APIEndpoint, EndpointConfig

from ..dto.detail import OperatorDetail
from ..dto.response import OperatorResponse


class Operator(APIEndpoint):
    """Operators

    Provides access to operator operations including listing,
    retrieving, creating, and updating operators.
    """

    def get_config(self) -> EndpointConfig:
        return EndpointConfig(
            endpoint=self._CAPABILITIES.features.operator_groups.operator_groups,
            dto_list=OperatorResponse,
            dto_retrieve=OperatorDetail,
        )
