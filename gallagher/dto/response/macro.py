""" Macro Response

"""

from typing import List

from ..utils import AppBaseResponseWithFollowModel
from ..summary.macro import MacroSummary


class MacroResponse(AppBaseResponseWithFollowModel):
    """Macro Response

    A response containing a list of macros with pagination support.
    """

    results: List[MacroSummary]
