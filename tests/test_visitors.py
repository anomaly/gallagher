""" Test Visitors endpoints

"""

import pytest

from gallagher.cc import APIClient

from gallagher.dto.detail import VisitorDetail
from gallagher.dto.response import VisitorResponse


@pytest.fixture
async def visitor_summary(api_client: APIClient) -> VisitorResponse:
    """Makes a single call to the visitor list"""
    response = await api_client.visitors.list()
    return response


async def test_visitor_list(visitor_summary: VisitorResponse):
    """Test listing visitors"""
    assert type(visitor_summary) is VisitorResponse
    assert type(visitor_summary.results) is list
    if not visitor_summary.results:
        pytest.skip('No visitors present in the test environment.')
    assert len(visitor_summary.results) > 0


async def test_visitor_detail(
    api_client: APIClient,
    visitor_summary: VisitorResponse,
):
    """Test getting the details of a visitor"""
    for v_summary in visitor_summary.results:
        v_detail = await api_client.visitors.retrieve(v_summary.id)
        assert type(v_detail) is VisitorDetail
        assert v_detail.id == v_summary.id
