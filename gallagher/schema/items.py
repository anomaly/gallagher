"""


"""

from typing import Optional

from .utils import AppBaseModel, IdentityMixin,\
    HrefMixin


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


class ItemResponse(
    AppBaseModel,
):
    """ 
    """
    results: list[ItemSummary]
    next: Optional[HrefMixin]

class ItemTypesResponse(
    AppBaseModel,
):
    """ 
    """
    item_types: list[ItemTypeDetail]
