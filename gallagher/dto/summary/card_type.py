from typing import Optional

from ..utils import (
    AppBaseModel,
    IdentityMixin,
)

class CardExpiryTypeSummary(AppBaseModel):
    expiry_type: Optional[str] = None


class CardSummary(
    AppBaseModel,
    IdentityMixin,
):
    """Card summary as sent by the Event objects

    Note: that we should revise this if required

    """

    facility_code: str
    number: str
    issue_level: int
