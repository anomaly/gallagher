""" Events that the Command Centre

Command Centre has about 80 event types that occur when somebody 
authenticates at a device, usually by badging a card.
"""

from ..utils import (
    APIBase,
    EndpointConfig
)


class Event(
    APIBase
):
    """

    """

    __config__ = EndpointConfig(
        endpoint="events",
        dto_list=EventResponse,
        dto_retrieve=EventDetail,
    )
