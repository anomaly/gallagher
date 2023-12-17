"""

"""
from typing import Optional

from .utils import (
    AppBaseModel,
    HrefMixin,
    IdentityMixin,
)

from ..dto.alarm import AlarmRef
from ..dto.cardholder import CardholderRef
from ..dto.access_group import AccessGroupRef
from ..dto.door import DoorRef


class EventTypeSummary(
    AppBaseModel,
    IdentityMixin,
):
    """ An event type has identifiers and names
    """
    name: str


class EventSummary(
    AppBaseModel,
    IdentityMixin,
    HrefMixin
):
    """ Events that the Command Centre generates

    """
    server_display_name: str
    time: str
    message: Optional[str]
    occurrences: int
    priority: int

    # Hrefs to follows other events
    next: HrefMixin
    previous: HrefMixin
    updates: HrefMixin


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
    group: str
    type: str
    event_type: EventTypeSummary
    division: str
    cardholder: str
    entry_access_zone: str
    exit_access_zone: str
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
