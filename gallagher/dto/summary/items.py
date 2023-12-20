
from ..utils import (
    AppBaseModel,
    IdentityMixin,
    HrefMixin
)


class ItemTypeDetail(
    AppBaseModel,
):
    """ Items Types only provide the name and id

    This is used by the discovery endpoint and is used by
    the ItemTypesResponse
    """
    id: str
    name: str
    canonical_type_name: str


class ItemSummary(
    AppBaseModel,
    HrefMixin,
    IdentityMixin,
):
    """ Summary of an Item which adds the notes and 
    server_display_name, this is used by the item summary response
    """
    name: str
    type: ItemTypeDetail
