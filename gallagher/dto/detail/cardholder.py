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


class CardholderDetail(
    AppBaseModel,
    IdentityMixin,
):
    """ Displays a table of cardholders

    Gallagher command centre offers a summary of all the cardholders
    provisioned on the system. This command presents a summary table
    with the aim of using the identifier to get detailed information.

    """
    first_name: str
    last_name: str
    short_name: Optional[str] = None
    description: Optional[str] = None
    authorised: bool

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
