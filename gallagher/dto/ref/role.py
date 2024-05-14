"""
"""

from ..utils import (
    AppBaseModel,
    HrefMixin,
)

class RoleRef(
    AppBaseModel,
    HrefMixin,
):
    name: str
    