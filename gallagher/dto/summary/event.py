from typing import Optional

from gallagher.dto.utils import (
    AppBaseModel,
    HrefMixin,
    IdentityMixin,
)

from ..summary import (
    EventTypeSummary
)


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
