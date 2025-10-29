from typing import Optional
from datetime import datetime

from ..utils import AppBaseModel, IdentityMixin, HrefMixin

from ..ref import DivisionRef


class RoleDetail(AppBaseModel, IdentityMixin, HrefMixin):
    """ """

    id: Optional[str] = None
    name: str
    description: Optional[str] = None
    serverDisplayName: Optional[str] = None
    division: Optional[dict] = None
    active: Optional[bool] = None
    created: Optional[datetime] = None
    modified: Optional[datetime] = None
