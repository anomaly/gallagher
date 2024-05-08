"""


"""

import pytest

from gallagher.dto.summary import (
    ItemSummary,
)

from gallagher.dto.response import (
    ItemTypesResponse,
    ItemsSummaryResponse,
)

from gallagher.cc.alarms.items import (
    Item
)

@pytest.fixture
async def items_types() -> ItemTypesResponse:
    """ Get a list of item types and iterates through it
    these are a summary response

    """
    from gallagher.cc.alarms.items import (
        ItemsTypes
    )

    response = await ItemsTypes.list()
    return response

@pytest.fixture
async def items_summary() -> ItemsSummaryResponse:
    """ Get a list of items and this should feed into fetching
    each one of these on it's own.

    """
    response = await Item.list()
    return response


async def test_items_types_list(
    items_types: ItemTypesResponse
):
    """ Get a list of item types and iterates through it
    these are a summary response

    """

    assert type(items_types) is ItemTypesResponse
    assert type(items_types.item_types) is list
    assert len(items_types.item_types) > 0


async def test_items_list(items_summary: ItemsSummaryResponse):
    """ Get a list of items and this should feed into fetching
    each one of these on it's own.

    """

    assert type(items_summary) is ItemsSummaryResponse
    assert type(items_summary.results) is list
    assert len(items_summary.results) > 0


async def test_items_follow_next(items_summary: ItemsSummaryResponse):
    """ Get a list of items and this should feed into fetching
    each one of these on it's own.

    """

    assert type(items_summary) is ItemsSummaryResponse
    assert type(items_summary.results) is list
    assert len(items_summary.results) > 0

    follow_item_summary = items_summary

    while follow_item_summary.next:
        # Get the next page if there is one
        # assign it to the summary and keep it going
        follow_item_summary = await Item.next(follow_item_summary)
        assert type(follow_item_summary) is ItemsSummaryResponse
        assert type(follow_item_summary.results) is list
        assert len(follow_item_summary.results) > 0


async def test_item_detail(items_summary: ItemsSummaryResponse):
    """ Get each item in the list and make sure it's a valid item

    """
    for item_summary in items_summary.results:
        # Get the detail of the item
        item_detail_response = await Item.retrieve(item_summary.id)
        assert type(item_detail_response) is ItemSummary
        assert (item_detail_response.id == item_summary.id)
