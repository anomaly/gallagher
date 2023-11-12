"""


"""

from typing import Optional

from .utils import (
    AppBaseModel,
    IdentityMixin,
    HrefMixin
)

class CardExpiryType(
    AppBaseModel
):
    expiry_type: Optional[str] = None

class CardTypeDetail(
    AppBaseModel,
    IdentityMixin,
    HrefMixin
):
    """ Card Types are cards mobile or physical that are supported at a site
    """
    name: str
    minimum_number: Optional[str] = None
    maximum_number: Optional[str] = None
    initial_card_state: str
    facility_code: str
    credential_class: str
    available_card_states: list[str] = None
    default_expiry: Optional[CardExpiryType] = None
    send_registration_email: Optional[bool] = False
    send_registration_sms: Optional[bool] = False

class CardTypeResponse(
    AppBaseModel,
):
    """ Card Types are cards mobile or physical that are supported at a site
    """
    results: list[CardTypeDetail]
    next: Optional[HrefMixin] = None
