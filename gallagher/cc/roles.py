""" Roles

"""

from gallagher.cc.core import APIEndpoint, EndpointConfig

from ..dto.detail import RoleDetail
from ..dto.response import RoleResponse


class Roles(APIEndpoint):
    """Roles

    Provides access to role operations including listing,
    retrieving, creating, and updating roles.
    """

    def get_config(self) -> EndpointConfig:
        return EndpointConfig(
            endpoint=self._CAPABILITIES.features.roles.roles,
            dto_list=RoleResponse,
            dto_retrieve=RoleDetail,
        )
