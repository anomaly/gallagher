"""


"""

from typing import Optional

from .utils import AppBaseModel, IdentityMixin,\
    HrefMixin

class CardTypeDetail(
    AppBaseModel,
    IdentityMixin,
    HrefMixin
):
    """ Card Types are cards mobile or physical that are supported at a site
    """
    name: str
    minimum_number: Optional[str]
    maximum_number: Optional[str]
    initial_card_state: str
    facility_code: str
    credential_class: str
    available_card_states: list[str]

class CardTypeResponse(
    AppBaseModel,
):
    """ Card Types are cards mobile or physical that are supported at a site
    """
    results: list[CardTypeDetail]
    next: Optional[HrefMixin]
