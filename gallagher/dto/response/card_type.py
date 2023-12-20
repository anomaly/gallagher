from typing import Optional

from ..utils import (
    AppBaseModel,
    HrefMixin
)

from ..detail import (
    CardTypeDEtail
)


class CardTypeResponse(
    AppBaseModel,
):
    """ Card Types are cards mobile or physical that are supported at a site
    """
    results: list[CardTypeDetail]
    next: Optional[HrefMixin] = None
