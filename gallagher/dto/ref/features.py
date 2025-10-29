""" Features Reference

"""

from ..utils import AppBaseModel, HrefMixin


class FeaturesRef(
    AppBaseModel,
    HrefMixin
):
    """Features Reference

    A reference to features containing minimal information
    for linking and identification purposes.
    """

    id: str
    name: str
