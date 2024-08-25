""" Cardholder related 

"""

from ..core import Capabilities, APIEndpoint, EndpointConfig

from ...dto.detail import (
    CardholderDetail,
    PdfDetail,
)

from ...dto.response import (
    CardholderSummaryResponse,
    PdfResponse,
)


class Cardholder(APIEndpoint):
    """Cardholder endpoints allow you to search for and retrieve cardholder details.

    Cardholders are the users of the system and are the entities that are
    granted access to doors. Cardholders can be people, vehicles, or other
    entities that require access to the site.
    """

    @classmethod
    async def get_config(cls) -> EndpointConfig:
        return EndpointConfig(
            endpoint=Capabilities.CURRENT.features.cardholders.cardholders,
            dto_list=CardholderSummaryResponse,
            dto_retrieve=CardholderDetail,
        )

class PdfDefinition(APIEndpoint):
    """PDF Definitions provide a list of support PDF definitions for the instance.

    These can vary between using physical cards, mobile credentials, or
    biometrics. The card type is used to dynamically determine the types
    of credentials available on this particular instance.
    """

    @classmethod
    async def get_config(cls) -> EndpointConfig:
        return EndpointConfig(
            endpoint=Capabilities.CURRENT.features.personal_data_fields\
                .personal_data_fields,
            dto_list=PdfResponse,
            dto_retrieve=PdfDetail,
        )


__shillelagh__ = (
    Cardholder,
)