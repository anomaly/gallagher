""" Interlock Groups

"""

from gallagher.cc.core import APIEndpoint, EndpointConfig

from ..dto.detail import InterlockGroupDetail
from ..dto.response import InterlockGroupResponse


class InterlockGroup(APIEndpoint):
    """Interlock Groups

    Provides access to interlock group operations including listing
    and retrieving interlock groups. Interlock groups enforce rules
    between doors so that only one can be open at a time.
    """

    def get_config(self) -> EndpointConfig:
        return EndpointConfig(
            endpoint=self._CAPABILITIES.features.interlock_groups.interlock_groups,
            dto_list=InterlockGroupResponse,
            dto_retrieve=InterlockGroupDetail,
        )
