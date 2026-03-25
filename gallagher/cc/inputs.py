""" Inputs

"""

from gallagher.cc.core import APIEndpoint, EndpointConfig

from ..dto.detail import InputDetail
from ..dto.response import InputResponse


class Input(APIEndpoint):
    """Inputs

    Provides access to input operations including listing and
    retrieving inputs. Inputs are hardware monitoring points
    such as door contacts, motion detectors, and alarm triggers.
    """

    def get_config(self) -> EndpointConfig:
        return EndpointConfig(
            endpoint=self._CAPABILITIES.features.inputs.inputs,
            dto_list=InputResponse,
            dto_retrieve=InputDetail,
        )
