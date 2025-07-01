""" Access Groups

"""

from gallagher.cc.core import Capabilities, APIEndpoint, EndpointConfig

from ..dto.detail import AccessGroupDetail
from ..dto.response import AccessGroupResponse


class AccessGroups(APIEndpoint):
    """Access Groups

    Provides access to access group operations including listing,
    retrieving, creating, and updating access groups.
    """

    @classmethod
    async def get_config(cls) -> EndpointConfig:
        return EndpointConfig(
            endpoint=Capabilities.CURRENT.features.access_groups.access_groups,
            dto_list=AccessGroupResponse,
            dto_retrieve=AccessGroupDetail,
        )
