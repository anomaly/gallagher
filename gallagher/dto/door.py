"""


"""

from .utils import (
    AppBaseModel,
    IdentityMixin,
    HrefMixin
)


class DoorRef(
    AppBaseModel,
    HrefMixin
):
    """ Door 

    """
    name: str


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
