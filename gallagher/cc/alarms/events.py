""" Events that the Command Centre

Command Centre has about 80 event types that occur when somebody 
authenticates at a device, usually by badging a card.
"""

from ..core import Capabilities, APIEndpoint, EndpointConfig

from ...dto.detail import (
    EventDetail,
)

from ...dto.response import (
    EventTypeResponse,
    EventSummaryResponse,
)


class Event(APIEndpoint):
    """Event"""

    @classmethod
    async def get_config(cls) -> EndpointConfig:
        return EndpointConfig(
            endpoint=Capabilities.CURRENT.features.events.events,
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
