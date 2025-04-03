from ..utils import AppBaseModel, OptionalHrefMixin


class ItemRef(AppBaseModel, OptionalHrefMixin):
    """Reference to an ItemType"""

    name: str
