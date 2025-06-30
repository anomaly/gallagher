""" Access Group Reference

"""

from ..utils import AppBaseModel, HrefMixin


class AccessGroupRef(
    AppBaseModel,
    HrefMixin
):
    """Access Group Reference

    A reference to an access group containing minimal information
    for linking and identification purposes.
    """

    id: str
    name: str
