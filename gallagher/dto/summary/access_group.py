from typing import Optional
from datetime import datetime

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
    DivisionRef,
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
    IdentityMixin,
    HrefMixin
):
    """Access Group Summary

    A summary view of an access group containing key information
    for listing and basic operations.
    """

    name: str
    description: Optional[str] = None
    division: Optional[DivisionRef] = None
    cardholder_count: Optional[int] = None
    created: Optional[datetime] = None
    modified: Optional[datetime] = None


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

    valid_from: from_optional_datetime = None  # Appears as from in the API
    valid_until: until_optional_datetime = None
