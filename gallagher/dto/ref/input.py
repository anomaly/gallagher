from ..utils import AppBaseModel, HrefMixin


class InputRef(
    AppBaseModel,
    HrefMixin,
):
    """Reference to an Input"""

    id: str
    name: str
