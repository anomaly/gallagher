from gallagher.dto.utils import (
    AppBaseModel,
)


class DoorSummaryResponse(
    AppBaseModel
):
    """

    """
    results: list[DoorSummary]
