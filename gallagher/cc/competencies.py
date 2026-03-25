""" Competencies

"""

from gallagher.cc.core import APIEndpoint, EndpointConfig

from ..dto.detail import CompetencyDetail
from ..dto.response import CompetencyResponse


class Competency(APIEndpoint):
    """Competencies

    Provides access to competency operations including listing
    and retrieving competencies. Competencies represent operator
    skills or qualifications tracked by the command centre.
    """

    def get_config(self) -> EndpointConfig:
        return EndpointConfig(
            endpoint=self._CAPABILITIES.features.competencies.competencies,
            dto_list=CompetencyResponse,
            dto_retrieve=CompetencyDetail,
        )
