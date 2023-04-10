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
    """ Personal Data Fields are custom fields for a card holder
    """
    name: str


class ItemSummary(
    ItemRef,
    IdentityMixin,
):
    """ Personal Data Fields are custom fields for a card holder
    """
    type: ItemTypeDetail
    notes: Optional[str]
    server_display_name: Optional[str]


class ItemResponse(
    AppBaseModel,
):
    """ Personal Data Fields are custom fields for a card holder
    """
    results: list[ItemSummary]
    next: Optional[HrefMixin]