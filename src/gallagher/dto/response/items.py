from typing import Optional

from ..utils import (
    AppBaseModel,
    HrefMixin
)

from ..summary import (
    ItemSummary,
    ItemTypeSummary
)


class ItemsSummaryResponse(
    AppBaseModel,
):
    """  ItemsResponse is the list of items from the API
    it provides the summary of all Items Summary
    """
    results: list[ItemSummary]
    next: Optional[HrefMixin] = None


class ItemTypesResponse(
    AppBaseModel,
):
    """ Every security centre can provide a list of item types

    While the response is rather abridged, this is the detail form
    of the Item Types.
    """
    item_types: list[ItemTypeSummary]
