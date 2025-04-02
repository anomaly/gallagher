""" Events that the Command Centre

Command Centre has about 80 event types that occur when somebody 
authenticates at a device, usually by badging a card.
"""

from ..core import (
    Capabilities,
    APIEndpoint,
    EndpointConfig,
)

from ...dto.detail import (
    EventDetail,
)

from ...dto.response import (
    EventTypeResponse,
    EventSummaryResponse,
)


class Event(APIEndpoint):
    """Event
    
    How updates differ from GET:

    - events.updates.href as found in /api discovery, it will give you the 
      first events that arrive after you call the endpoint.
    - the url in updates in /api/events or /api/events/updates, returns
      events that arrive at the bookmark and meet the search criteria.

    the next href is a non blocking call to get the next set of events.
    """

    @classmethod
    async def get_config(cls) -> EndpointConfig:
        return EndpointConfig(
            endpoint=Capabilities.CURRENT.features.events.events,
            endpoint_follow=Capabilities.CURRENT.features.events.updates,
            dto_follow=EventSummaryResponse,
            dto_list=EventSummaryResponse,
            dto_retrieve=EventDetail,
        )

class EventType(APIEndpoint):
    """EventType"""

    @classmethod
    async def get_config(cls) -> EndpointConfig:
        return EndpointConfig(
            endpoint=Capabilities.CURRENT.features.events.event_groups,
            dto_list=EventTypeResponse,
        )


class EventGroups(APIEndpoint):
    """ Event Groups are used to filter events
    
    Use this to dynamically discover a list of event groups which you can
    then use for various updates from the command centre.

    See above Event class for more details.
    """

    @classmethod
    async def get_config(cls) -> EndpointConfig:
        return EndpointConfig(
            endpoint=Capabilities.CURRENT.features.events.event_groups,
            dto_list=EventTypeResponse,
        )
