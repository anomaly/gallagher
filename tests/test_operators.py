""" Test Operators endpoints

"""

import pytest

from gallagher.cc import APIClient

from gallagher.dto.detail import OperatorDetail
from gallagher.dto.response import OperatorResponse

@pytest.fixture
async def operator_summary(api_client: APIClient) -> OperatorResponse:
    """Makes a single call to the operator list"""
    response = await api_client.operators.list()
    return response


async def test_operator_list(operator_summary: OperatorResponse):
    """Test listing operators"""
    assert type(operator_summary) is OperatorResponse
    assert type(operator_summary.results) is list
    assert len(operator_summary.results) > 0


async def test_operator_detail(
    api_client: APIClient,
    operator_summary: OperatorResponse,
):
    """Test getting the details of an operator"""
    for o_summary in operator_summary.results:
        if not o_summary.id:
            pytest.skip('Operator summary missing id, cannot retrieve detail.')
        o_detail = await api_client.operators.retrieve(o_summary.id)
        assert type(o_detail) is OperatorDetail
        assert o_detail.id == o_summary.id
