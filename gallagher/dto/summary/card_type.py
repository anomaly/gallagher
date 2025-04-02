from typing import Optional

from ..utils import (
    AppBaseModel,
    OptionalIdentityMixin,
)

class CardExpiryTypeSummary(AppBaseModel):
    expiry_type: Optional[str] = None


class CardSummary(
    AppBaseModel,
    OptionalIdentityMixin,
):
    """Card summary as sent by the Event objects

    Note: that we should revise this if required

    """

    facility_code: str
    number: str
    issue_level: int
