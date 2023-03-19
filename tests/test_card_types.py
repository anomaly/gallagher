
"""

"""

def test_get_card_types():
    from gallagher.cc import CardType
    from gallagher.schema import Response

    response = CardType.list()
    assert type(response) is Response
    assert type(response.results) is list
    assert len(response.results) > 0