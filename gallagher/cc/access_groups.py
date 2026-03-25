""" Access Groups

"""

from gallagher.cc.core import APIEndpoint, EndpointConfig

from ..dto.detail import AccessGroupDetail
from ..dto.response import AccessGroupResponse


class AccessGroup(APIEndpoint):
    """Access Groups

    Provides access to access group operations including listing,
    retrieving, creating, and updating access groups.
    """

    def get_config(self) -> EndpointConfig:
        return EndpointConfig(
            endpoint=self._CAPABILITIES.features.access_groups.access_groups,
            dto_list=AccessGroupResponse,
            dto_retrieve=AccessGroupDetail,
        )
