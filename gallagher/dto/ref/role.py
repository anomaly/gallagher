""" Role Reference

"""

from ..utils import AppBaseModel, HrefMixin


class RoleRef(
    AppBaseModel,
    HrefMixin
):
    """Role Reference

    A reference to a role containing minimal information
    for linking and identification purposes.
    """

    id: str
    name: str
