""" Events that the Command Centre

Command Centre has about 80 event types that occur when somebody 
authenticates at a device, usually by badging a card.
"""

from ..core import (
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

    def get_config(self) -> EndpointConfig:
        return EndpointConfig(
            endpoint=self._CAPABILITIES.features.events.events,
            endpoint_follow=self._CAPABILITIES.features.events.updates,
            dto_follow=EventSummaryResponse,
            dto_list=EventSummaryResponse,
            dto_retrieve=EventDetail,
        )

class EventType(APIEndpoint):
    """EventType"""

    def get_config(self) -> EndpointConfig:
        return EndpointConfig(
            endpoint=self._CAPABILITIES.features.events.event_groups,
            dto_list=EventTypeResponse,
        )


class EventGroups(APIEndpoint):
    """ Event Groups are used to filter events
    
    Use this to dynamically discover a list of event groups which you can
    then use for various updates from the command centre.

    See above Event class for more details.
    """

    def get_config(self) -> EndpointConfig:
        return EndpointConfig(
            endpoint=self._CAPABILITIES.features.events.event_groups,
            dto_list=EventTypeResponse,
        )
