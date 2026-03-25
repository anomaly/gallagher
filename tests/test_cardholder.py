""" Cardholders

"""

import random
import pytest

from gallagher.cc import APIClient

from gallagher.dto.detail import (
    CardholderDetail,
)

from gallagher.dto.response import CardholderSummaryResponse


@pytest.fixture
async def cardholder_summary(api_client: APIClient) -> CardholderSummaryResponse:
    """Makes a single call to the cardholder list

    This is passed as a fixture to all other calls around
    on this test to save network round trips.

    :return: CardholderSummaryResponse
    """

    response = await api_client.cardholders.list()
    return response


async def test_cardholder_list(cardholder_summary: CardholderSummaryResponse):
    """Test for the cardholder list"""
    assert type(cardholder_summary) is CardholderSummaryResponse
    assert type(cardholder_summary.results) is list
    assert len(cardholder_summary.results) > 0


async def test_cardholder_search(
    api_client: APIClient,
    cardholder_summary: CardholderSummaryResponse,
):
    """Test for the cardholder search"""

    # Get a random cardholder in the list
    cardholder = random.choice(cardholder_summary.results)

    # Search for the cardholder
    search_results = await api_client.cardholders.search(
        name=cardholder.first_name,
    )

    # We should fine at least one cardholder with the same name
    assert type(search_results) is CardholderSummaryResponse
    assert len(search_results.results) > 0


async def test_cardholder_detail(
    api_client: APIClient,
    cardholder_summary: CardholderSummaryResponse,
):
    """For each cardholder in the list, get the detail and compare"""

    for cardholder_summary in cardholder_summary.results:
        if not cardholder_summary.id:
            pytest.skip(
                'Cardholder summary missing id, cannot retrieve detail.')
        # Get the detail of the cardholder for comparison
        cardholder_detail_response = await api_client.cardholders\
            .retrieve(cardholder_summary.id)
        assert type(cardholder_detail_response) is CardholderDetail
        assert cardholder_detail_response.id == cardholder_summary.id

        # For each personal_data_definition attempt to access it via
        # the wrapper and compare values
        for pdf in cardholder_detail_response.personal_data_definitions:
            # see if it's access via the shortcut
            pdf_attr_name = pdf.name[1:].replace(' ', '_').lower()
            # first test to see there is an accessible value
            assert getattr(cardholder_detail_response.pdf, pdf_attr_name) \
                is not None
            # then compare the values, this should work because
            # the model_validator would have assigned this via reference
            assert getattr(cardholder_detail_response.pdf, pdf_attr_name) \
                == pdf.contents
