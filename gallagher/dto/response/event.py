from typing import Optional

from ..utils import (
    AppBaseModel,
    HrefMixin,
    IdentityMixin,
)

from ..ref import (
    AlarmRef,
    CardholderRef,
    DoorRef,
    AccessZoneRef,
    DivisionRef,
)

from ..summary import (
    EventGroupSummary,
    EventTypeSummary,
    CardholderSummary,
)


class EventSummaryResponse(
    AppBaseModel,
    HrefMixin,
    IdentityMixin,
):
    """
    """
    server_display_name: str
    time: str
    message: Optional[str]
    occurrences: int
    priority: int
    alarm: AlarmRef

    operator: CardholderRef
    source: str
    group: EventGroupSummary
    type: EventTypeSummary
    event_type: EventTypeSummary
    division: DivisionRef
    cardholder: CardholderSummary
    entry_access_zone: AccessZoneRef
    exit_access_zone: AccessZoneRef
    door: DoorRef
    access_group: HrefMixin
    card: str
    modified_item: str

    next: HrefMixin
    previous: HrefMixin
    updates: HrefMixin


class EventTypeResponse(
    AppBaseModel,
):
    """ Event Type Response

    Event Type Responses return a set of eventGroups which in turn
    has identifiers, names and event types.

    """
    event_groups: list[EventGroupSummary]
