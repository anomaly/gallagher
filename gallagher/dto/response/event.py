from typing import Optional

from gallagher.dto.utils import (
    AppBaseModel,
    HrefMixin,
    IdentityMixin,
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
    # alarm: AlarmRef

    # operator: CardholderRef
    # source: str
    # group: str
    # type: str
    # event_type: EventTypeSummary
    # division: str
    # cardholder: str
    # entry_access_zone: str
    # exit_access_zone: str
    # door: DoorRef
    # access_group: HrefMixin
    # card: str
    # modified_item: str

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
