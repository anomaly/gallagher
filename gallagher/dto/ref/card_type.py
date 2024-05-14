"""
"""

from ..utils import (
    AppBaseModel,
    IdentityMixin,
    HrefMixin,
    OptionalHrefMixin,
)

class CardTypeRef(
    AppBaseModel,
    HrefMixin,
):
    """ Reference for a card type """
    name: str