""" Cardholder Detail """
from typing import Optional

from ..ref import (
    CardholderExtendedRef,
    DivisionRef,
    PlaceholderRef,
    RoleRef,
)

from ..summary import (
    CardholderCardSummary,
)

from ..utils import (
    AppBaseModel,
    IdentityMixin,
    HrefMixin,
)

class CardholderRelationshipDetail(
    AppBaseModel,
    HrefMixin,
):
    role: RoleRef
    cardholder: CardholderExtendedRef
    

class CardholderDetail(
    AppBaseModel,
    IdentityMixin,
):
    """Displays a table of cardholders

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

    # personal_data_definitions
    cards: list[CardholderCardSummary] = []
    # access_groups
    # operator_groups
    # competencies

    edit: HrefMixin
    update_location: HrefMixin
    notes: Optional[str] = None

    # notifications
    relationships: list[CardholderRelationshipDetail] = []
    # lockers
    # elevator_groups
    updates: PlaceholderRef
    # redactions

    def get_pdf(self, PDFRef):
        """Get a parsed PDF field from the cardholder given the PDF Ref

        This assumes that you have access to the right PDF reference from
        the singleton that the API client would have parsed on initialisation.

        For validation you must pass the PDFRef object to this method.
        """
        pass

    def __rich_repr__(self):
        return (
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
        )
