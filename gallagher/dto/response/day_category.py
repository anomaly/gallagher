from typing import Optional

from ..utils import (
    HrefMixin,
    AppBaseResponseWithFollowModel,
)

from ..ref import (
    DayCategoryRef,
)


class DayCategoryResponse(
    AppBaseResponseWithFollowModel,
):
    """The response has a list of results and a link to the next page"""

    results: list[DayCategoryRef]
