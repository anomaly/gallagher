""" Visits

"""

from gallagher.cc.core import APIEndpoint, EndpointConfig
from ..dto.detail import VisitDetail
from ..dto.response import VisitResponse


class Visit(APIEndpoint):
    """Visits
    Provides access to visit operations including listing, retrieving, creating, and updating visits.
    """
    def get_config(self) -> EndpointConfig:
        return EndpointConfig(
            endpoint=self._CAPABILITIES.features.visits.visits,
            dto_list=VisitResponse,
            dto_retrieve=VisitDetail,
        )
