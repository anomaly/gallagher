""" Test Macro endpoints

"""

import pytest

from gallagher.cc import APIClient
from gallagher.dto.detail import MacroDetail
from gallagher.dto.response import MacroResponse
from gallagher.cc.macros import Macro


@pytest.fixture
async def macro_summary(api_client: APIClient) -> MacroResponse:
    """Makes a single call to the macro list"""
    response = await api_client.macros.list()
    return response


async def test_macro_list(macro_summary: MacroResponse):
    """Test listing macros"""
    assert type(macro_summary) is MacroResponse
    assert type(macro_summary.results) is list
    assert len(macro_summary.results) > 0


async def test_macro_detail(
    api_client: APIClient,
    macro_summary: MacroResponse,
):
    """Test getting the details of a macro"""
    for m_summary in macro_summary.results:
        m_detail = await api_client.macros.retrieve(m_summary.id)
        assert type(m_detail) is MacroDetail
        assert m_detail.id == m_summary.id
