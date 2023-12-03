""" Events that the Command Centre

Command Centre has about 80 event types that occur when somebody 
authenticates at a device, usually by badging a card.
"""

from ..core import (
    APIEndpoint,
    EndpointConfig
)


class Event(
    APIEndpoint
):
    """

    """

    @classmethod
    def get_config(cls):
        return EndpointConfig(
            endpoint="events",
            dto_list=EventResponse,
            dto_retrieve=EventDetail,
        )
