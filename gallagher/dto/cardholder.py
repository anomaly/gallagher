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

    def cli_repr(self):
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
    """

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

    @property
    def cli_repr(self):
        return [x.cli_repr() for x in self.results]

    def __str__(self):
        return f"{len(self.results)} cardholders"
