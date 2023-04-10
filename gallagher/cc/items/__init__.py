from ..utils import APIBase


class ItemsTypes(APIBase):
    """
     Gallagher
    """
    ENDPOINT = "items/types"

class Item(APIBase):
    """
    Gallagher advises against hardcoding the URLs for divisions, and instead
    recommends using the /api endpoint to discover the URLs from 
    events.divisions.href and alarms.division.href.
    
    """

    ENDPOINT = "items"

