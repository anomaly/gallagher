""" Visitors

"""

from gallagher.cc.core import APIEndpoint, EndpointConfig

from ..dto.detail import VisitorDetail
from ..dto.response import VisitorResponse


class Visitors(APIEndpoint):
    """Visitors

    Provides access to visitor operations including listing,
    retrieving, creating, and updating visitors.
    """

    def get_config(self) -> EndpointConfig:
        return EndpointConfig(
            endpoint=self._CAPABILITIES.features.visits.visits,
            dto_list=VisitorResponse,
            dto_retrieve=VisitorDetail,
        )
