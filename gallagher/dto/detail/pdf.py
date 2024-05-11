from typing import Optional

from ..utils import (
    AppBaseModel,
    IdentityMixin,
    HrefMixin,
)


class PdfDetail(AppBaseModel, HrefMixin):
    """Personal Data Fields are custom fields for a card holder"""

    name: str
    description: Optional[str]
    division: IdentityMixin
    server_display_name: Optional[str]
