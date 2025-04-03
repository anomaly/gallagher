from typing import Optional
from datetime import datetime

from ..utils import (
    AppBaseModel,
    HrefMixin,
    IdentityMixin,
    OptionalHrefMixin,
)

from ..ref import (
    AlarmRef,
    CardholderRef,
    CardholderExtendedRef,
    DoorRef,
    AccessZoneRef,
    DivisionRef,
    ItemRef,
    EventGroupRef,
)

from .card_type import (
    CardSummary,
)

from .items import (
    ItemSummary,
)


class EventTypeSummary(
    AppBaseModel,
    IdentityMixin,
):
    """An event type has identifiers and names"""

    name: str


class EventGroupSummary(
    AppBaseModel,
    IdentityMixin,
):
    """Event Groups are a collection of event types

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
    """Summary of events that have occurred on the server"""

    server_display_name: Optional[str] = None
    time: datetime
    message: Optional[str] = None
    occurrences: Optional[int] = 0
    priority: int
    alarm: Optional[AlarmRef] = None

    operator: Optional[CardholderRef] = None
    source: ItemRef
    group: Optional[EventGroupRef] = None
    type: Optional[EventTypeSummary] = None
    event_type: Optional[EventTypeSummary] = None
    division: Optional[DivisionRef] = None
    cardholder: Optional[CardholderExtendedRef] = None
    entry_access_zone: Optional[AccessZoneRef] = None
    exit_access_zone: Optional[AccessZoneRef] = None
    door: Optional[DoorRef] = None
    access_group: OptionalHrefMixin = None
    card: Optional[CardSummary] = None
    modified_item: Optional[ItemSummary] = None
