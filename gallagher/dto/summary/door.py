from ..utils import AppBaseModel, IdentityMixin, HrefMixin


class DoorSummary(
    AppBaseModel,
    IdentityMixin,
    HrefMixin,
):
    """ """

    name: str
