from ..utils import (
    AppBaseResponseModel,
    AppBaseResponseWithFollowModel,
)

from ..summary import (
    EventGroupSummary,
    EventSummary,
)

class EventSummaryResponse(
    AppBaseResponseWithFollowModel,
):
    """ Event Summary Response
    """

    events: list[EventSummary]

class EventTypeResponse(
    AppBaseResponseModel,
):
    """Event Type Response

    Event Type Responses return a set of eventGroups which in turn
    has identifiers, names and event types.
    """

    event_groups: list[EventGroupSummary]

