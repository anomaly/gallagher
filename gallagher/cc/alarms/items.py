""" Items


"""

from ..core import (
    Capabilities,
    APIEndpoint,
    EndpointConfig,
)

from ...dto.items import (
    ItemTypesResponse,
    ItemsSummaryResponse,
    ItemDetail
)


class ItemsTypes(APIEndpoint):
    """
     Gallagher
    """

    @classmethod
    def get_config(cls):
        return EndpointConfig(
            endpoint=Capabilities.CURRENT.features.items.item_types.href,
            dto_list=ItemTypesResponse,
            dto_retrieve=ItemTypesResponse,
        )


class Item(APIEndpoint):
    """
    Gallagher advises against hardcoding the URLs for divisions, and instead
    recommends using the /api endpoint to discover the URLs from 
    events.divisions.href and alarms.division.href.

    """

    @classmethod
    def get_config(cls):
        return EndpointConfig(
            endpoint=Capabilities.CURRENT.features.items.items.href,
            dto_list=ItemsSummaryResponse,
            dto_retrieve=ItemDetail,
        )
