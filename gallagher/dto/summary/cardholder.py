from typing import Optional
from typing_extensions import Annotated

from datetime import datetime

from pydantic import Field

from ..ref import (
    CardTypeRef,
)

from ..utils import (
    AppBaseModel,
    IdentityMixin,
    HrefMixin,
)


class CardholderSummary(
    AppBaseModel,
    IdentityMixin,
    HrefMixin,
):
    """
    The cardholder search at /api/cardholders returns an array of these.
    It is a subset of what you get from a cardholder's detail page at
    /api/cardholders/{id}

    (linked as the href in this object), to be more suitable for large result sets.
    """

    first_name: str
    last_name: str
    short_name: Optional[str] = None
    description: Optional[str] = None
    authorised: bool = False

    def __rich_repr__(self):
        return [
            self.id,
            self.first_name,
            self.last_name,
            "yes" if self.authorised else "no",
        ]

    def __str__(self):
        return f"{self.id} {self.first_name} {self.last_name}"


class CardholderCardStatusSummary(
    AppBaseModel,
):
    """ Used by CardholderCardSummary to show the status of an assigned card
    """
    value: str
    type: str


from_datetime = Annotated[
    Optional[datetime],
    Field(..., alias="from")
]

class CardholderCardSummary(
    AppBaseModel,
    HrefMixin,
):
    """ A card assigned to a cardholder, note that these are not the same as
    the card objects themselves, they miss a few fields that the card object
    has and are only used in the context of a cardholder's detail page.
    
    These children objects are referenced by their `href` as they aren't assigned
    an identifier object in the system.
    """
    number: str
    card_serial_number: Optional[str] = None
    issue_level: int

    status: CardholderCardStatusSummary

    type: CardTypeRef
    valid_from: Optional[from_datetime] = None
    until: Optional[datetime] = None
    credential_class: str
    trace: bool = False
    last_printed_or_encoded_time: Optional[datetime] = None
    last_printed_or_encoded_issue_level: int = 0
    pin: Optional[str] = None # Leading zeros are significant
    visitor_contractor: bool = False
    owned_by_site: bool = False
    credential_id: str = "reserved" # TODO: Reserved for future use?
    ble_facility_id: str = "reserved" # TODO: Reserved for future use?

