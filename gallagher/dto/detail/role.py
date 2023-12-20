from typing import Optional

from gallagher.dto.utils import (
    AppBaseModel,
    IdentityMixin,
    HrefMixin
)

from ..ref import (
    DivisionRef
)


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
