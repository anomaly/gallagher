from typing import Optional

from ..utils import (
    HrefMixin,
    AppBaseResponseWithNavModel,
)

from ..detail import (
    CardTypeDetail
)


class CardTypeResponse(
    AppBaseResponseWithNavModel,
):
    """ Card Types are cards mobile or physical that are supported at a site
    """
    results: list[CardTypeDetail]
