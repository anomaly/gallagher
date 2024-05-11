from ..utils import AppBaseModel, HrefMixin


class DoorRef(AppBaseModel, HrefMixin):
    """Door"""

    name: str
