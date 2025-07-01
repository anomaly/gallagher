""" Visitor Reference

"""

from ..utils import AppBaseModel, HrefMixin


class VisitorRef(
    AppBaseModel,
    HrefMixin
):
    """Visitor Reference

    A reference to a visitor containing minimal information
    for linking and identification purposes.
    """

    id: str
    first_name: str
    last_name: str
