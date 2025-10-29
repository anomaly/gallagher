""" Locker Reference

"""

from ..utils import AppBaseModel, HrefMixin


class LockerRef(
    AppBaseModel,
    HrefMixin
):
    """Locker Reference

    A reference to a locker containing minimal information
    for linking and identification purposes.
    """

    id: str
    name: str
    bank_id: str
