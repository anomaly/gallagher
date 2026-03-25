""" Outputs

"""

from gallagher.cc.core import APIEndpoint, EndpointConfig

from ..dto.detail import OutputDetail
from ..dto.response import OutputResponse


class Output(APIEndpoint):
    """Outputs

    Provides access to output operations including listing and
    retrieving outputs. Outputs are hardware control points
    such as relays, sirens, and locking devices.
    """

    def get_config(self) -> EndpointConfig:
        return EndpointConfig(
            endpoint=self._CAPABILITIES.features.outputs.outputs,
            dto_list=OutputResponse,
            dto_retrieve=OutputDetail,
        )
