from typing import Optional

from ..utils import (
    HrefMixin,
    AppBaseResponseModel,
    AppBaseResponseWithFollowModel,
)

from ..summary import ItemSummary, ItemTypeSummary


class ItemsSummaryResponse(
    AppBaseResponseWithFollowModel,
):
    """ItemsResponse is the list of items from the API
    it provides the summary of all Items Summary
    """

    results: list[ItemSummary]


class ItemTypesResponse(
    AppBaseResponseModel,
):
    """Every security centre can provide a list of item types

    While the response is rather abridged, this is the detail form
    of the Item Types.
    """

    item_types: list[ItemTypeSummary]
