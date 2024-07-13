""" Cardholder Detail """
from typing import Optional, Any
from typing_extensions import Self

from pydantic import model_validator, Field

from ..utils import (
    AppBaseModel,
    IdentityMixin,
    HrefMixin,
)

from ..ref import (
    CardholderExtendedRef,
    DivisionRef,
    PlaceholderRef,
    RoleRef,
)

from ..summary import (
    CardholderCardSummary,
    CardholderAccessGroupSummary,
    PdfSummary,
)

class CardholderRelationshipDetail(
    AppBaseModel,
    HrefMixin,
):
    """ A role that a cardholder has 

    Think of this as a representation of a many to many relationship
    where this cardholder has a role in the system. Other users can
    have the same role.
    """
    role: RoleRef
    cardholder: CardholderExtendedRef


class CardholderPersonalDataField(
    AppBaseModel,
    HrefMixin,
):
    """ A PDF field as defined in the Cardholders personal data

    A definition that defines the cardholder's personal data. This
    is essentially the Summary of the Pdf field, along with a string
    value, which also is accessible using the key at the dictionary level.
    """
    definition: PdfSummary
    value: str | HrefMixin
    notifications: Optional[bool] = False # Local to the @Email field

class CardholderPersonalDataDefinition(
    AppBaseModel,
):
    """ A personal data definition for the cardholder

    This is sent back as the personalDataDefinitions field in the
    CardholderDetail response. It has a peculiar structure that 
    we have outlined in the parse_personal_data_definitions method
    """
    name: str
    contents: CardholderPersonalDataField


class PdfAccessorWrapper:
    """ Wrapper that holds a dictionary of accessible PDF 

    The aim is to make these accessible in as python a way as possible

    Note: this is not a pydantic class, and is used as a placeholder
    to dynamically populate the dictionary of personal data fields
    """
    pass
    
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

    personal_data_definitions: list[CardholderPersonalDataDefinition] = []
    cards: list[CardholderCardSummary] = []
    access_groups: list[CardholderAccessGroupSummary] = []
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

    # Note this is not a pyndatic class and hence utils.py
    # has the configuration set to allow arbitrary types
    pdf: PdfAccessorWrapper = PdfAccessorWrapper()

    @model_validator(mode='before')
    @classmethod
    def parse_personal_data_definitions(cls, data: Any) -> Any:
        """ Rewrite the personalDataDefinition for it to be parseable

        The personalDataDefinitions field is a list of objects, each one of 
        which has a single object with key being the personal data field name
        and the value being the value of the field.

        This method rewrites that to be an object with name and contents fields
        which allows us to use pydantic to parse it and make it available to the
        user as a list of objects.

        The results of this will also be used to dynamically parse the values
        for the cardholder's PDF fields.
        """

        if 'personalDataDefinitions' in data:
            data['personalDataDefinitions'] = [
                {
                    'name': name, 
                    'contents': contents
                } \
                    for item in data['personalDataDefinitions'] \
                    for name, contents in item.items()
            ]

        return data
    
    @model_validator(mode='after')
    def populate_pdf_accessor(self) -> Self:
        # For each key in the personal_data_definitions, create a new
        # attribute on the pdf object with the key as the name
        for pdf_field in self.personal_data_definitions:
            # Note this sets a reference from personal_data_definitions
            # if you compare these in the tests, they should be the same
            setattr(
                self.pdf, 
                # replace spaces with underscores and make it lowercase
                # ignore the prefixed @ symbol
                pdf_field.name[1:].replace(' ', '_').lower(),
                pdf_field.contents
            )

        return self

    def __rich_repr__(self):
        return (
            f"[blue bold] person",
            f"{'id':>20} {self.id}",
            f"{'first name':>20} {self.first_name}",
            f"{'last name':>20} {self.last_name}",
            f"{'short name':>20} {self.short_name}",
            f"{'description':>20} {self.description}",
            f"{'authorised':>20} {'yes' if self.authorised else 'no'}",
            f"",
            f"{'disable cipher pad':>20} {'yes' if self.disable_cipher_pad else 'no'}",
            f"{'division':>20} {self.division.id}",
            f"[blue bold] hrefs",
            f"{'edit':>20} [link={self.edit.href}]edit[/link]",
        )
