""" Test Operators endpoints

"""

import pytest

from gallagher.dto.detail import OperatorDetail
from gallagher.dto.response import OperatorResponse
from gallagher.cc.operators import Operators


@pytest.fixture
async def operator_summary() -> OperatorResponse:
    """Makes a single call to the operator list"""
    response = await Operators.list()
    return response


async def test_operator_list(operator_summary: OperatorResponse):
    """Test listing operators"""
    assert type(operator_summary) is OperatorResponse
    assert type(operator_summary.results) is list
    assert len(operator_summary.results) > 0


async def test_operator_detail(operator_summary: OperatorResponse):
    """Test getting the details of an operator"""
    for o_summary in operator_summary.results:
        o_detail = await Operators.retrieve(o_summary.id)
        assert type(o_detail) is OperatorDetail
        assert o_detail.id == o_summary.id
