""" Card references """
from typing import Optional

from ..utils import (
    AppBaseModel,
    IdentityMixin,
    HrefMixin,
)

class CardTypeRef(
    AppBaseModel,
    HrefMixin,
):
    name: str
    