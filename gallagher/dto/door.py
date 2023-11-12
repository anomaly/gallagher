"""


"""

from .utils import (
    AppBaseModel,
    IdentityMixin,
    HrefMixin
)


class DoorSummary(
    AppBaseModel,
    IdentityMixin,
    HrefMixin,
):
    """

    """
    name: str


class DoorSummaryResponse(
    AppBaseModel
):
    """

    """
    results: list[DoorSummary]
