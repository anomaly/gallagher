""" Items


"""

from ..core import (
    Capabilities,
    APIEndpoint,
    EndpointConfig,
)

from ...dto.summary import (
    ItemSummary,
)
from ...dto.response import (
    ItemTypesResponse,
    ItemsSummaryResponse,
)


class ItemsTypes(APIEndpoint):
    """
    Gallagher
    """

    @classmethod
    async def get_config(cls) -> EndpointConfig:
        return EndpointConfig(
            endpoint=Capabilities.CURRENT.features.items.item_types,
            endpoint_follow=Capabilities.CURRENT.features.items.updates,
            dto_follow=ItemsSummaryResponse,
            dto_list=ItemTypesResponse,
            dto_retrieve=ItemTypesResponse,
        )
    
    @classmethod
    async def updates(cls, href: str) -> bool:
        """Follow updates on an item

        Arguments:
        cls: class reference
        href: href to follow
        """
        return await cls.follow(href)


class Item(APIEndpoint):
    """
    Gallagher advises against hardcoding the URLs for divisions, and instead
    recommends using the /api endpoint to discover the URLs from
    events.divisions.href and alarms.division.href.

    """

    @classmethod
    async def get_config(cls) -> EndpointConfig:
        return EndpointConfig(
            endpoint=Capabilities.CURRENT.features.items.items,
            dto_list=ItemsSummaryResponse,
            dto_retrieve=ItemSummary,
        )
