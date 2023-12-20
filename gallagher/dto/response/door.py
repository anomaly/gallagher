from ..utils import (
    AppBaseModel,
)


class DoorSummaryResponse(
    AppBaseModel
):
    """

    """
    results: list[DoorSummary]
