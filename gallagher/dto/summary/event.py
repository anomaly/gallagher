from typing import Optional

from ..utils import (
    AppBaseModel,
    HrefMixin,
    IdentityMixin,
    OptionalHref,
)

from ..ref import (
    AlarmRef,
    CardholderRef,
    CardholderEventRef,
    DoorRef,
    AccessZoneRef,
    DivisionRef,
    ItemRef,
)

from .cardholder import (
    CardholderSummary,
)


class EventTypeSummary(
    AppBaseModel,
    IdentityMixin,
):
    """ An event type has identifiers and names
    """
    name: str


class EventGroupSummary(
    AppBaseModel,
    IdentityMixin,
):
    """ Event Groups are a collection of event types

    Each group has names and event types. This is usually used
    in an Event Type Response.
    """
    name: str
    event_types: list[EventTypeSummary]


class EventSummary(
    AppBaseModel,
    HrefMixin,
    IdentityMixin,
):
    """ Summary of events that have occurred on the server
    """
    server_display_name: Optional[str] = None
    time: str
    message: Optional[str] = None
    occurrences: Optional[int] = 0
    priority: int
    alarm: Optional[AlarmRef] = None

    operator: Optional[CardholderRef] = None
    source: ItemRef
    # group: Optional[EventGroupSummary] = None
    type: Optional[EventTypeSummary] = None
    event_type: Optional[EventTypeSummary] = None
    division: Optional[DivisionRef] = None
    cardholder: Optional[CardholderEventRef] = None
    entry_access_zone: Optional[AccessZoneRef] = None
    exit_access_zone: Optional[AccessZoneRef] = None
    door: Optional[DoorRef] = None
    access_group: OptionalHref = None
    # card: str
    # modified_item: str
