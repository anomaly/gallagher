"""

"""
from typing import Optional
from datetime import datetime

from .utils import (
    AppBaseModel,
    IdentityMixin,
    HrefMixin,
)

from .division import (
    DivisionRef,
)


class CardholderRef(
    AppBaseModel,
    HrefMixin,
):
    """ Reference to a Cardholder
    """
    name: str


class CardholderSummary(
    AppBaseModel,
    IdentityMixin
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
    authorised: bool

    def __rich_repr__(self):
        return [
            self.id,
            self.first_name,
            self.last_name,
            "yes" if self.authorised else "no"
        ]

    def __str__(self):
        return f"{self.id} {self.first_name} {self.last_name}"


class CardholderDetail(
    CardholderSummary
):
    """ Displays a table of cardholders

    Gallagher command centre offers a summary of all the cardholders
    provisioned on the system. This command presents a summary table
    with the aim of using the identifier to get detailed information.

    """
    disable_cipher_pad: bool = False
    division: DivisionRef
    edit: HrefMixin

    operator_login_enabled: bool = False
    operator_password_expired: bool = False

    update_location: HrefMixin
    updates: HrefMixin

    user_extended_access_time: bool = False
    windows_login_enabled: bool = False

    def __rich_repr__(self):
        return [
            f"[blue bold] person",
            f"{'id':>20} {self.id}",
            f"{'first_name':>20} {self.first_name}",
            f"{'last_name':>20} {self.last_name}",
            f"{'short_name':>20} {self.short_name}",
            f"{'description':>20} {self.description}",
            f"{'authorised':>20} {'yes' if self.authorised else 'no'}",
            f"",
            f"{'disable_cipher_pad':>20} {'yes' if self.disable_cipher_pad else 'no'}",
            f"{'division':>20} {self.division.id}",
            f"[blue bold] hrefs",
            f"{'edit':>20} [link={self.edit.href}]edit[/link]",
        ]


class CardholderSummaryResponse(
    AppBaseModel
):
    """ Summary response for cardholder list and search

    /api/cardholders is generally the endpoint that 

    """
    results: list[CardholderSummary]

    @property
    def cli_header(self):
        return [
            "Id",
            "First name",
            "Last name",
            "Authorised"
        ]

    def __rich_repr__(self):
        return [r.__rich_repr__() for r in self.results]

    def __str__(self):
        return f"{len(self.results)} cardholders"
