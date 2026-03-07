""" Test Input endpoints

"""

import pytest

from gallagher.cc import APIClient
from gallagher.dto.detail import InputDetail
from gallagher.dto.response import InputResponse
from gallagher.cc.inputs import Input


@pytest.fixture
async def input_summary(api_client: APIClient) -> InputResponse:
    """Makes a single call to the input list"""
    response = await api_client.inputs.list()
    return response


async def test_input_list(input_summary: InputResponse):
    """Test listing inputs"""
    assert type(input_summary) is InputResponse
    assert type(input_summary.results) is list
    assert len(input_summary.results) > 0


async def test_input_detail(
    api_client: APIClient,
    input_summary: InputResponse,
):
    """Test getting the details of an input"""
    for i_summary in input_summary.results:
        i_detail = await api_client.inputs.retrieve(i_summary.id)
        assert type(i_detail) is InputDetail
        assert i_detail.id == i_summary.id
