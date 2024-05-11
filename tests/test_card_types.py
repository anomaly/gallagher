""" Card types tests

"""

import pytest

from gallagher.dto.response import CardTypeResponse

from gallagher.cc.cardholders.card_type import CardType


@pytest.fixture
async def card_types() -> CardTypeResponse:
    """Makes a single call to the card type list

    This is passed as a fixture to all other calls around
    on this test to save network round trips.

    :return: CardTypeResponse
    """

    response = await CardType.list()
    return response


async def test_get_card_types(card_types: CardTypeResponse):
    """Test if test card type"""

    assert type(card_types) is CardTypeResponse
    assert type(card_types.results) is list
    assert len(card_types.results) > 0
