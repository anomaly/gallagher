from typing import Optional

from ..utils import (
    AppBaseModel,
    HrefMixin,
    IdentityMixin,
)

from ..ref import (
    DivisionRef,
    AccessGroupRef,
)

from ..enum import PdfType


class PdfDetail(AppBaseModel, IdentityMixin, HrefMixin):
    """Personal Data Fields are custom fields for a card holder"""

    id: Optional[str] = None
    name: str
    server_display_name: Optional[str] = None
    description: Optional[str] = None
    division: Optional[dict] = None
    type: Optional[str] = None
    default: Optional[str] = None
    required: Optional[bool] = None
    unique: Optional[bool] = None
    default_access: Optional[str] = None
    operator_access: Optional[str] = None
    sort_priority: Optional[int] = None

    access_groups: Optional[list] = None

    regex: Optional[str] = None
    regex_description: Optional[str] = None
    notification_default: Optional[bool] = None
    image_width: Optional[int] = None
    image_height: Optional[int] = None
    image_format: Optional[str] = None
    content_type: Optional[str] = None
    is_profile_image: Optional[bool] = None

    accessGroups: Optional[list] = None
