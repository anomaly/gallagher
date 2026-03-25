from ..utils import AppBaseModel, HrefMixin


class OutputRef(
    AppBaseModel,
    HrefMixin,
):
    """Reference to an Output"""

    id: str
    name: str
