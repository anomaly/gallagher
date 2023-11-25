"""
"""
from ..core import (
    APIEndpoint,
    EndpointConfig
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

    __config__ = EndpointConfig(
        endpoint=cls.paths.features.alarms.alarms.href,
        dto_list=ItemTypesResponse,
    )


class Item(APIEndpoint):
    """
    Gallagher advises against hardcoding the URLs for divisions, and instead
    recommends using the /api endpoint to discover the URLs from 
    events.divisions.href and alarms.division.href.

    """

    __config__ = EndpointConfig(
        endpoint="items",
        dto_list=ItemsSummaryResponse,
        dto_retrieve=ItemDetail,
    )
