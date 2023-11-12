from ..utils import APIBase
from ...dto.items import (
    ItemTypesResponse,
    ItemsSummaryResponse,
    ItemDetail
)


class ItemsTypes(APIBase):
    """
     Gallagher
    """

    class Config:

        endpoint = "items/types"
        list_response_class = ItemTypesResponse


class Item(APIBase):
    """
    Gallagher advises against hardcoding the URLs for divisions, and instead
    recommends using the /api endpoint to discover the URLs from 
    events.divisions.href and alarms.division.href.

    """

    class Config:

        endpoint = "items"
        list_response_class = ItemsSummaryResponse
        retrieve_response_class = ItemDetail
