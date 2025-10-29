""" Salto Response

"""

from typing import List

from ..utils import AppBaseResponseWithFollowModel
from ..summary import SaltoSummary


class SaltoResponse(AppBaseResponseWithFollowModel):
    """Salto Response

    A response containing a list of Salto devices with pagination support.
    """

    results: List[SaltoSummary]
