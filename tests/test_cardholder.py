""" Cardholders

"""

import pytest

from gallagher.dto.detail import (
    CardholderDetail,
)

from gallagher.dto.response import CardholderSummaryResponse

from gallagher.cc.cardholders import Cardholder


@pytest.fixture
async def cardholder_summary() -> CardholderSummaryResponse:
    """Makes a single call to the cardholder list

    This is passed as a fixture to all other calls around
    on this test to save network round trips.

    :return: CardholderSummaryResponse
    """

    response = await Cardholder.list()
    return response


async def test_cardholder_list(cardholder_summary: CardholderSummaryResponse):
    """Test for the cardholder list"""
    assert type(cardholder_summary) is CardholderSummaryResponse
    assert type(cardholder_summary.results) is list
    assert len(cardholder_summary.results) > 0


async def test_cardholder_detail(cardholder_summary: CardholderSummaryResponse):
    """For each cardholder in the list, get the detail and compare"""

    for cardholder_summary in cardholder_summary.results:
        # Get the detail of the cardholder for comparison
        cardholder_detail_response = await Cardholder.retrieve(cardholder_summary.id)
        assert type(cardholder_detail_response) is CardholderDetail
        assert cardholder_detail_response.id == cardholder_summary.id
