"""

"""

from ..core import APIEndpoint, EndpointConfig

from ...dto.response import CardTypeResponse


class CardType(APIEndpoint):
    """Card Types provide a list of support card types for the instance.

    These can vary between using physical cards, mobile credentials, or
    biometrics. The card type is used to dynamically determine the types
    of credentials available on this particular instance.
    """

    def get_config(self) -> EndpointConfig:
        return EndpointConfig(
            endpoint=self._CAPABILITIES.features.card_types.card_types,
            dto_list=CardTypeResponse,
            dto_retrieve=CardTypeResponse,
        )
    