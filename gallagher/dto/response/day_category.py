from typing import Optional

from ..utils import (
    HrefMixin,
    AppBaseResponseWithNavModel,
)

from ..ref import (
    DayCategoryRef,
)


class DayCategoryResponse(
    AppBaseResponseWithNavModel,
):
    """ The response has a list of results and a link to the next page
    """

    results: list[DayCategoryRef]
