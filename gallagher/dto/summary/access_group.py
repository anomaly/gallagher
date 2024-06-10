from typing import Optional

from ..utils import (
    AppBaseModel,
    IdentityMixin,
    HrefMixin,
    OptionalHrefMixin,
    TypeValuePair,
    from_optional_datetime,
    until_optional_datetime,
)

from ..ref import (
    AccessGroupRef,
    AccessZoneRef,
    ScheduleRef,
)


class AccessSummary(
    AppBaseModel,
    HrefMixin,
):
    """Access is zone paired with a schedule"""

    access_zone: AccessZoneRef
    schedule: ScheduleRef


class AccessGroupSummary(
    AppBaseModel,
):
    """AccessGroup Summary is what the API returns on searches

    This builds on the Ref class to add the summary fields and is
    extended by the Detail class to add the fully remainder of
    the fields
    """

    name: str
    description: Optional[str]
    parent: Optional[AccessGroupRef]
    division: IdentityMixin
    cardholders: OptionalHrefMixin
    server_display_name: Optional[str]



class CardholderAccessGroupSummary(
    AppBaseModel,
    HrefMixin,
):
    """ An Access Group assigned to a cardholder.

    Essentially when an access group is assigned to a cardholder
    it inherits the properties and additionally a start and end date
    """
    access_group: AccessGroupRef
    status: TypeValuePair

    valid_from: from_optional_datetime = None # Appears as from in the API
    valid_until: until_optional_datetime = None
