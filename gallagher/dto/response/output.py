""" Output Response

"""

from typing import List

from ..utils import AppBaseResponseWithFollowModel
from ..summary.output import OutputSummary


class OutputResponse(AppBaseResponseWithFollowModel):
    """Output Response

    A response containing a list of outputs with pagination support.
    """

    results: List[OutputSummary]
