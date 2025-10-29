"""
"""

from ..utils import (
    AppBaseModel,
    OptionalHrefMixin,
)

class CardTypeRef(
    AppBaseModel,
    OptionalHrefMixin,
):
    """ Reference for a card type """
    name: str