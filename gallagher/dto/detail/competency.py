""" Competency Detail

"""

from typing import Optional

from ..summary.competency import CompetencySummary


class CompetencyDetail(CompetencySummary):
    """Competency Detail

    A detailed view of a competency containing all information
    for comprehensive operations and management.
    """

    notes: Optional[str] = None
    cardholder_count: Optional[int] = None
