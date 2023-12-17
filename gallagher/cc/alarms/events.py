""" Events that the Command Centre

Command Centre has about 80 event types that occur when somebody 
authenticates at a device, usually by badging a card.
"""

from ..core import (
    Capabilities,
    APIEndpoint,
    EndpointConfig
)

from ...dto.event import (
    EventTypeResponse,
)


class Event(
    APIEndpoint
):
    """ Event 

    """

    @classmethod
    def get_config(cls):
        return EndpointConfig(
            endpoint=Capabilities.CURRENT.features.events.events,
            dto_list=EventResponse,
            dto_retrieve=EventDetail,
        )


class EventType(
    APIEndpoint
):
    """ EventType

    """

    @classmethod
    def get_config(cls):
        return EndpointConfig(
            endpoint=Capabilities.CURRENT.features.events.event_groups,
            dto_list=EventTypeResponse,
        )
