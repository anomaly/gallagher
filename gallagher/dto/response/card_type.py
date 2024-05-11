from typing import Optional

from ..utils import (
    HrefMixin,
    AppBaseResponseWithFollowModel,
)

from ..detail import CardTypeDetail


class CardTypeResponse(
    AppBaseResponseWithFollowModel,
):
    """Card Types are cards mobile or physical that are supported at a site"""

    results: list[CardTypeDetail]
