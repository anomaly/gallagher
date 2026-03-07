""" Macros

"""

from gallagher.cc.core import APIEndpoint, EndpointConfig

from ..dto.detail import MacroDetail
from ..dto.response import MacroResponse


class Macro(APIEndpoint):
    """Macros

    Provides access to macro operations including listing and
    retrieving macros. Macros are pre-configured automated
    sequences of actions that can be triggered on demand.
    """

    def get_config(self) -> EndpointConfig:
        return EndpointConfig(
            endpoint=self._CAPABILITIES.features.macros.macros,
            dto_list=MacroResponse,
            dto_retrieve=MacroDetail,
        )
