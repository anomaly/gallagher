""" Elevator Groups

"""

from gallagher.cc.core import APIEndpoint, EndpointConfig

from ..dto.detail import ElevatorDetail
from ..dto.response import ElevatorResponse


class Elevator(APIEndpoint):
    """Elevator Groups

    Provides access to elevator group operations including listing
    and retrieving elevator groups. Elevator groups define which
    floors cardholders can access via elevator control.
    """

    def get_config(self) -> EndpointConfig:
        return EndpointConfig(
            endpoint=self._CAPABILITIES.features.elevators.elevator_groups,
            dto_list=ElevatorResponse,
            dto_retrieve=ElevatorDetail,
        )
