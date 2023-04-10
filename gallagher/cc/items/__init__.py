from ..utils import APIBase
from ...schema.items import ItemResponse, ItemTypesResponse


class ItemsTypes(APIBase):
    """
     Gallagher
    """

    ENDPOINT = "items/types"
    RESPONSE_CLASS = ItemTypesResponse

class Item(APIBase):
    """
    Gallagher advises against hardcoding the URLs for divisions, and instead
    recommends using the /api endpoint to discover the URLs from 
    events.divisions.href and alarms.division.href.
    
    """

    ENDPOINT = "items"
    RESPONSE_CLASS = ItemResponse

