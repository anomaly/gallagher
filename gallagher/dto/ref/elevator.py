from ..utils import AppBaseModel, HrefMixin


class ElevatorRef(
    AppBaseModel,
    HrefMixin,
):
    """Reference to an Elevator Group"""

    id: str
    name: str
