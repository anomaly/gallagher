from ..utils import AppBaseModel, HrefMixin


class MacroRef(
    AppBaseModel,
    HrefMixin,
):
    """Reference to a Macro"""

    id: str
    name: str
