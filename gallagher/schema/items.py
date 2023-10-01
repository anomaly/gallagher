"""


"""

from typing import Optional

from .utils import (
    AppBaseModel,
    IdentityMixin,
    HrefMixin
)

from .division import DivisionRef

class ItemTypeDetail(
    AppBaseModel,
):
    """ Items Types only provide the name and id

    This is used by the discovery endpoint and is used by
    the ItemTypesResponse
    """
    id: str
    name: str

class ItemRef(
    AppBaseModel,
    HrefMixin
):
    """ Reference to an ItemType
    """
    name: str


class ItemSummary(
    ItemRef,
    IdentityMixin,
):
    """ Summary of an Item which adds the notes and 
    server_display_name, this is used by the item summary response
    """
    type: ItemTypeDetail
    notes: Optional[str]
    server_display_name: Optional[str]

class ItemDetail(
    ItemSummary,
):
    """ All attributes of the Summary plus the division

    While running our tests we found that for some system level
    objects the divison can be optional, this attribute is hence
    marked optional, please test for availability before using it.
    """
    division: Optional[DivisionRef]
    

class ItemsSummaryResponse(
    AppBaseModel,
):
    """  ItemsResponse is the list of items from the API
    it provides the summary of all Items Summary
    """
    results: list[ItemSummary]
    next: Optional[HrefMixin]

class ItemTypesResponse(
    AppBaseModel,
):
    """ Every security centre can provide a list of item types

    While the response is rather abridged, this is the detail form
    of the Item Types.
    """
    item_types: list[ItemTypeDetail]
