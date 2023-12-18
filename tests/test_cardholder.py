"""

"""


async def test_cardholder_list():

    from gallagher.cc.cardholders.cardholders import Cardholder
    from gallagher.dto.cardholder import CardholderSummaryResponse

    response = await Cardholder.list()
    assert type(response) is CardholderSummaryResponse
    assert type(response.results) is list
    assert len(response.results) > 0


async def test_cardholder_detail():

    from gallagher.cc.cardholders.cardholders import Cardholder
    from gallagher.dto.cardholder import (
        CardholderSummaryResponse,
        CardholderDetail,
    )

    response = await Cardholder.list()
    assert type(response) is CardholderSummaryResponse

    for cardholder_summary in response.results:
        # Get the detail of the cardholder for comparison
        cardholder_detail_response = await Cardholder.retrieve(
            cardholder_summary.id
        )
        assert type(cardholder_detail_response) is CardholderDetail
        assert (cardholder_detail_response.id == cardholder_summary.id)
