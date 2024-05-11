""" Personal Data Fields tests

Personal Data Fields are dynamic fields that can be added on a cardholder.
These are per site and are local to the customer.

See #1 to track how this was developed and tested.
"""

import pytest

from gallagher.dto.response import PdfResponse

from gallagher.cc.cardholders.cardholders import PdfDefinition


@pytest.fixture
async def pdf_definition() -> PdfResponse:
    """Makes a single call to the pdf list

    This is passed as a fixture to all other calls around
    on this test to save network round trips.

    :return: PdfResponse
    """

    response = await PdfDefinition.list()
    return response


async def test_pdf_list(pdf_definition: PdfResponse):

    assert type(pdf_definition) is PdfResponse
    assert type(pdf_definition.results) is list
    assert len(pdf_definition.results) > 0


async def test_pdf_detail(pdf_definition: PdfResponse):

    for pdf in pdf_definition.results:
        detail = await PdfDefinition.detail(pdf.id)

        # assert type(detail) is PdfResponse
