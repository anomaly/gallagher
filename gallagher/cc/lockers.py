""" Lockers

"""

from gallagher.cc.core import APIEndpoint, EndpointConfig

from ..dto.detail import LockerDetail
from ..dto.response import LockerResponse


class Locker(APIEndpoint):
    """Lockers

    Provides access to locker operations including listing,
    retrieving, creating, and updating lockers.
    """

    def get_config(self) -> EndpointConfig:
        return EndpointConfig(
            endpoint=self._CAPABILITIES.features.locker_banks.locker_banks,
            dto_list=LockerResponse,
            dto_retrieve=LockerDetail,
        )
