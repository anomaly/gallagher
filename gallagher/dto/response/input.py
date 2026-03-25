""" Input Response

"""

from typing import List

from ..utils import AppBaseResponseWithFollowModel
from ..summary.input import InputSummary


class InputResponse(AppBaseResponseWithFollowModel):
    """Input Response

    A response containing a list of inputs with pagination support.
    """

    results: List[InputSummary]
