async def test_pdf_list():

    from gallagher.cc.cardholders.cardholders import (
        PdfDefinition
    )
    from gallagher.dto.response import (
        PdfResponse
    )

    response = await PdfDefinition.list()
    assert type(response) is PdfResponse
    assert type(response.results) is list
    assert len(response.results) > 0
