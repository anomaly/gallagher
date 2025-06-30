""" Roles

"""

from ..core import Capabilities, APIEndpoint, EndpointConfig

from ..dto.detail import RoleDetail
from ..dto.response import RoleResponse


class Roles(APIEndpoint):
    """Roles

    Provides access to role operations including listing,
    retrieving, creating, and updating roles.
    """

    @classmethod
    async def get_config(cls) -> EndpointConfig:
        return EndpointConfig(
            endpoint=Capabilities.CURRENT.features.roles.roles,
            dto_list=RoleResponse,
            dto_retrieve=RoleDetail,
        )
