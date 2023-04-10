

def test_items_types_list():
    from gallagher.cc.items import ItemsTypes
    from gallagher.schema import Response

    response = ItemsTypes.list()
    assert type(response) is Response
    assert type(response.results) is list
    assert len(response.results) > 0

def test_items_list():
    from gallagher.cc.items import Item
    from gallagher.schema import Response
    from gallagher.schema.items import ItemSummary

    response = Item.list()
    assert type(response) is Response
    assert type(response.results) is list
    assert len(response.results) > 0