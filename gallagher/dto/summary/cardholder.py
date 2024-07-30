from typing import Optional

from datetime import datetime

from pydantic import EmailStr

from ..utils import (
    AppBaseModel,
    IdentityMixin,
    HrefMixin,
    OptionalHrefMixin,
    from_optional_datetime,
    until_optional_datetime,
)

from ..ref import (
    CardTypeRef,
)

from ..enum import CredentialsClass

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
        return (
            self.id,
            self.first_name,
            self.last_name,
            "yes" if self.authorised else "no",
        )

    def __str__(self):
        return f"{self.id} {self.first_name} {self.last_name}"


class CardholderCardStatusSummary(
    AppBaseModel,
):
    """ Used by CardholderCardSummary to show the status of an assigned card
    """
    value: str
    type: str


class CardholderCardInvitationSummary(
    AppBaseModel,
    OptionalHrefMixin,
):
    """ Used by CardholderCardSummary to show status of an invitation

    Invitations are sent by the Gallagher system to a cardholder via
    email and then text messages for mobile credentials to activate
    the app.
    """
    email: Optional[EmailStr] = None
    mobile: Optional[str] = None
    single_factor_only: bool = False
    status: str

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
    issue_level: Optional[int] = None

    status: CardholderCardStatusSummary

    type: CardTypeRef

    invitation: Optional[CardholderCardInvitationSummary] = None

    valid_from: from_optional_datetime = None # Appears as from in the API
    valid_until: until_optional_datetime = None
    credential_class: CredentialsClass
    trace: bool = False
    last_printed_or_encoded_time: Optional[datetime] = None
    last_printed_or_encoded_issue_level: int = 0
    pin: Optional[str] = None # Leading zeros are significant
    visitor_contractor: bool = False
    owned_by_site: bool = False
    credential_id: str = "reserved" # TODO: Reserved for future use?
    # TODO: Reserved for future use?
    # Test instance returns an int when a mobile credential is assigned
    # the docs still suggest this should be a string instead, leaving this
    # here to check into the future
    ble_facility_id:  str | int = "reserved" 

