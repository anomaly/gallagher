""" Test Division endpoints

""" 

async def test_division_list():
    """ Test listing a division

    This will trigger the list operation in the Division endpoints

    https://gallaghersecurity.github.io/cc-rest-docs/ref/events.html
    """
    from gallagher.cc.alarms.divisions import (
        Division
    )
    from gallagher.dto.response import (
        DivisionSummaryResponse
    )

    response = await Division.list()
    assert type(response) is DivisionSummaryResponse
    assert type(response.results) is list
    assert len(response.results) > 0


async def test_division_detail():
    """ Test getting the details of a division

    This will trigger the list endpoint and then run the detail
    endpoint for each one of the items in the list and compare the id
    of the items in the list to the ones in the detail

    https://gallaghersecurity.github.io/cc-rest-docs/ref/events.html
    """
    from gallagher.cc.alarms.divisions import (
        Division
    )
    from gallagher.dto.detail import (
        DivisionDetail,
    )
    from gallagher.dto.response import (
        DivisionSummaryResponse,
    )

    response = await Division.list()
    assert type(response) is DivisionSummaryResponse
    assert type(response.results) is list

    for division_summary in response.results:
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