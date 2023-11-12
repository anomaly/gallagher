"""

"""


def test_get_card_types():
    from gallagher.cc.card.card_type import CardType
    from gallagher.dto.card_type import CardTypeResponse

    response = CardType.list()
    assert type(response) is CardTypeResponse
    assert type(response.results) is list
    assert len(response.results) > 0
