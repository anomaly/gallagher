""" Test Division endpoints

""" 

import pytest

from gallagher.dto.detail import (
    DivisionDetail,
)

from gallagher.dto.response import (
    DivisionSummaryResponse
)

from gallagher.cc.alarms.divisions import (
    Division
)

@pytest.fixture
async def division_summary() -> DivisionSummaryResponse:
    """ Makes a single call to the division list

    This is passed as a fixture to all other calls around
    on this test to save network round trips.

    :return: DivisionSummaryResponse
    """

    response = await Division.list()
    return response

async def test_division_list(division_summary: DivisionSummaryResponse):
    """ Test listing a division

    This will trigger the list operation in the Division endpoints

    https://gallaghersecurity.github.io/cc-rest-docs/ref/events.html
    """

    assert type(division_summary) is DivisionSummaryResponse
    assert type(division_summary.results) is list
    assert len(division_summary.results) > 0


async def test_division_detail(
    division_summary: DivisionSummaryResponse
):
    """ Test getting the details of a division

    This will trigger the list endpoint and then run the detail
    endpoint for each one of the items in the list and compare the id
    of the items in the list to the ones in the detail

    https://gallaghersecurity.github.io/cc-rest-docs/ref/events.html
    """

    for division_summary in division_summary.results:
        # Get the detail of the division
        division_detail_response = await Division.retrieve(
            division_summary.id
        )
        assert type(division_detail_response) is DivisionDetail
        assert division_detail_response.id == division_summary.id


async def test_remove_division():
    """ Test removing a division


    """
    pass