"""

"""
from ..core import (
    Capabilities,
    APIEndpoint,
    EndpointConfig
)

from ...dto.cardholder import (
    CardholderSummaryResponse,
    CardholderDetail,
)


class Cardholder(APIEndpoint):
    """ Cardholder endpoints allow you to search for and retrieve cardholder details.

    Cardholders are the users of the system and are the entities that are 
    granted access to doors. Cardholders can be people, vehicles, or other 
    entities that require access to the site. 
    """

    @classmethod
    def get_config(cls):
        return EndpointConfig(
            endpoint=Capabilities.CURRENT.features.cardholders.cardholders.href,
            dto_list=CardholderSummaryResponse,
            dto_retrieve=CardholderDetail,
        )
