"""


"""


async def test_items_types_list():
    """ Get a list of item types and iterates through it
    these are a summary response

    """
    from gallagher.cc.alarms.items import ItemsTypes
    from gallagher.dto.items import ItemTypesResponse

    response = await ItemsTypes.list()
    assert type(response) is ItemTypesResponse
    assert type(response.item_types) is list
    assert len(response.item_types) > 0


async def test_items_list():
    """ Get a list of items and this should feed into fetching
    each one of these on it's own.

    """
    from gallagher.cc.alarms.items import Item
    from gallagher.dto.items import ItemsSummaryResponse

    response = await Item.list()
    assert type(response) is ItemsSummaryResponse
    assert type(response.results) is list
    assert len(response.results) > 0


async def test_item_detail():
    """ Get each item in the list and make sure it's a valid item

    """
    from gallagher.cc.alarms.items import Item
    from gallagher.dto.items import (
        ItemsSummaryResponse,
        ItemDetail
    )

    response: ItemsSummaryResponse = await Item.list()
    assert type(response) is ItemsSummaryResponse

    for item_summary in response.results:
        # Get the detail of the item
        item_detail_response = await Item.retrieve(item_summary.id)
        assert type(item_detail_response) is ItemDetail
        assert (item_detail_response.id == item_summary.id)
