from ..utils import AppBaseModel, HrefMixin


class FenceZoneRef(
    AppBaseModel,
    HrefMixin,
):
    """Reference to a Fence Zone"""

    id: str
    name: str
