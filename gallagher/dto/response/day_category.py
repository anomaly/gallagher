from typing import Optional

from gallagher.dto.utils import (
    AppBaseModel,
    HrefMixin
)

from ..ref import (
    DayCategoryRef,
)


class DayCategoryResponse(
    AppBaseModel,
):
    """ The response has a list of results and a link to the next page
    """

    results: list[DayCategoryRef]
    next: Optional[HrefMixin] = None
