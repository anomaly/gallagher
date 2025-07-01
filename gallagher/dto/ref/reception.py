""" Reception Reference

"""

from ..utils import AppBaseModel, HrefMixin


class ReceptionRef(
    AppBaseModel,
    HrefMixin
):
    """Reception Reference

    A reference to a reception containing minimal information
    for linking and identification purposes.
    """

    id: str
    name: str
