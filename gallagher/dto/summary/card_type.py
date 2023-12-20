from typing import Optional

from gallagher.dto.utils import (
    AppBaseModel,
    IdentityMixin,
    HrefMixin
)


class CardExpiryTypeSummary(
    AppBaseModel
):
    expiry_type: Optional[str] = None
