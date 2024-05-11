from ..utils import (
    AppBaseResponseModel,
)

from ..summary import (
    DoorSummary,
)


class DoorSummaryResponse(
    AppBaseResponseModel,
):
    """ """

    results: list[DoorSummary]
