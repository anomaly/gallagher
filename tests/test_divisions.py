def test_division_list():
    from gallagher.cc.alarms.divisions import Division
    from gallagher.dto.division import DivisionDetailResponse

    response = Division.list()
    assert type(response) is DivisionDetailResponse
    assert type(response.results) is list
    assert len(response.results) > 0


def test_division_detail():
    from gallagher.cc.alarms.divisions import Division
    from gallagher.dto.division import (
        DivisionDetailResponse,
        DivisionDetail,
    )

    response = Division.list()
    assert type(response) is DivisionDetailResponse
    assert type(response.results) is list

    for division_summary in response.results:
        # Get the detail of the division
        division_detail_response = Division.retrieve(division_summary.id)
        assert type(division_detail_response) is DivisionDetail
        assert division_detail_response.id == division_summary.id
