""" Door Reference

"""

from ..utils import AppBaseModel, HrefMixin


class DoorRef(
    AppBaseModel,
    HrefMixin
):
    """Door Reference

    A reference to a door containing minimal information
    for linking and identification purposes.
    """

    id: str
    name: str
