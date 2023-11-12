"""

"""
from typing import Optional

from .utils import (
    AppBaseModel,
    IdentityMixin,
    HrefMixin
)

from .division import DivisionRef

class RoleDetail(
    AppBaseModel,
    IdentityMixin,
    HrefMixin
):
    """
    """
    name: str
    server_display_name: str
    description: Optional[str]
    division: DivisionRef

