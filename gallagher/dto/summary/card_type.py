from typing import Optional

from ..utils import (
    AppBaseModel,
    IdentityMixin,
    HrefMixin
)


class CardExpiryTypeSummary(
    AppBaseModel
):
    expiry_type: Optional[str] = None
