""" Test Output endpoints

"""

import pytest

from gallagher.cc import APIClient
from gallagher.dto.detail import OutputDetail
from gallagher.dto.response import OutputResponse
from gallagher.cc.outputs import Output


@pytest.fixture
async def output_summary(api_client: APIClient) -> OutputResponse:
    """Makes a single call to the output list"""
    response = await api_client.outputs.list()
    return response


async def test_output_list(output_summary: OutputResponse):
    """Test listing outputs"""
    assert type(output_summary) is OutputResponse
    assert type(output_summary.results) is list
    assert len(output_summary.results) > 0


async def test_output_detail(
    api_client: APIClient,
    output_summary: OutputResponse,
):
    """Test getting the details of an output"""
    for o_summary in output_summary.results:
        o_detail = await api_client.outputs.retrieve(o_summary.id)
        assert type(o_detail) is OutputDetail
        assert o_detail.id == o_summary.id
