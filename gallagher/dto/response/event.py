from typing import Optional

from ..utils import (
    AppBaseModel,
    HrefMixin,
    IdentityMixin,
)

from ..summary import (
    EventGroupSummary,
    EventSummary,
)


class EventSummaryResponse(
    AppBaseModel,
):

    events: list[EventSummary]

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
