""" Card references """
from typing import Optional

from ..utils import (
    AppBaseModel,
    HrefMixin,
)

class CardTypeRef(
    AppBaseModel,
    HrefMixin,
):
    name: str
    