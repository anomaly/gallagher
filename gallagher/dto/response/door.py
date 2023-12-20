from ..utils import (
    AppBaseModel,
)

from ..summary import (
    DoorSummary,
)


class DoorSummaryResponse(
    AppBaseModel
):
    """

    """
    results: list[DoorSummary]
