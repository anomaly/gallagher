async def test_division_list():
    from gallagher.cc.alarms.divisions import (
        Division
    )
    from gallagher.dto.response import (
        DivisionDetailResponse
    )

    response = await Division.list()
    assert type(response) is DivisionDetailResponse
    assert type(response.results) is list
    assert len(response.results) > 0


async def test_division_detail():
    from gallagher.cc.alarms.divisions import (
        Division
    )
    from gallagher.dto.detail import (
        DivisionDetail,
    )
    from gallagher.dto.response import (
        DivisionDetailResponse,
    )

    response = await Division.list()
    assert type(response) is DivisionDetailResponse
    assert type(response.results) is list

    for division_summary in response.results:
        # Get the detail of the division
        division_detail_response = await Division.retrieve(division_summary.id)
        assert type(division_detail_response) is DivisionDetail
        assert division_detail_response.id == division_summary.id
