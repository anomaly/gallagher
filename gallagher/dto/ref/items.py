from ..utils import AppBaseModel, HrefMixin


class ItemRef(AppBaseModel, HrefMixin):
    """Reference to an ItemType"""

    name: str
