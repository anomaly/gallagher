""" Lockers

"""

from gallagher.cc.core import Capabilities, APIEndpoint, EndpointConfig

from ..dto.detail import LockerDetail
from ..dto.response import LockerResponse


class Lockers(APIEndpoint):
    """Lockers

    Provides access to locker operations including listing,
    retrieving, creating, and updating lockers.
    """

    @classmethod
    async def get_config(cls) -> EndpointConfig:
        return EndpointConfig(
            endpoint=Capabilities.CURRENT.features.locker_banks.locker_banks,
            dto_list=LockerResponse,
            dto_retrieve=LockerDetail,
        )
