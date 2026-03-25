from ..utils import AppBaseModel, HrefMixin


class InterlockGroupRef(
    AppBaseModel,
    HrefMixin,
):
    """Reference to an Interlock Group"""

    id: str
    name: str
