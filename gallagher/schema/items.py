"""


"""

from typing import Optional

from .utils import AppBaseModel, IdentityMixin,\
    HrefMixin

from .division import DivisionRef

class ItemTypeDetail(
    AppBaseModel,
):
    """
    """
    id: str
    name: str

class ItemRef(
    AppBaseModel,
    HrefMixin
):
    """ 
    """
    name: str


class ItemSummary(
    ItemRef,
    IdentityMixin,
):
    """ 
    """
    type: ItemTypeDetail
    notes: Optional[str]
    server_display_name: Optional[str]

class ItemDetail(
    ItemSummary,
):
    """ All attributes of the Summary plus the division
    """
    division: DivisionRef
    

class ItemResponse(
    AppBaseModel,
):
    """  ItemsResponse is the list of items from the API
    """
    results: list[ItemSummary]
    next: Optional[HrefMixin]

class ItemTypesResponse(
    AppBaseModel,
):
    """ 
    """
    item_types: list[ItemTypeDetail]
