from typing import Optional

from ..utils import (
    AppBaseModel,
    HrefMixin,
)

from ..detail import (
    DivisionDetail
)


class DivisionDetailResponse(
    AppBaseModel
):
    """ Division

    """

    results: list[DivisionDetail]
    next: Optional[HrefMixin] = None
