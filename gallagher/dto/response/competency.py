""" Competency Response

"""

from typing import List

from ..utils import AppBaseResponseWithFollowModel
from ..summary.competency import CompetencySummary


class CompetencyResponse(AppBaseResponseWithFollowModel):
    """Competency Response

    A response containing a list of competencies with pagination support.
    """

    results: List[CompetencySummary]
