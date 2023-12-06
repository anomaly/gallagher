"""

"""
from ..core import (
    Capabilities,
    APIEndpoint,
    EndpointConfig
)

from ...dto.card_type import (
    CardTypeResponse
)


class CardType(APIEndpoint):
    """ Card Types provide a list of support card types for the instance.

    These can vary between using physical cards, mobile credentials, or
    biometrics. The card type is used to dynamically determine the types 
    of credentials available on this particular instance.  
    """

    @classmethod
    def get_config(cls):
        return EndpointConfig(
            endpoint=Capabilities.CURRENT.features.card_types.card_types,
            dto_list=CardTypeResponse,
            dto_retrieve=CardTypeResponse,
        )
