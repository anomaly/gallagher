""" Test Visits endpoints

"""

import pytest

from gallagher.cc import APIClient

from gallagher.dto.detail import VisitDetail
from gallagher.dto.response import VisitResponse


@pytest.fixture
async def visit_summary(api_client: APIClient) -> VisitResponse:
    """Makes a single call to the visit list"""
    response = await api_client.visits.list()
    return response


async def test_visit_list(visit_summary: VisitResponse):
    """Test listing visits"""
    assert type(visit_summary) is VisitResponse
    assert type(visit_summary.results) is list
    if not visit_summary.results:
        pytest.skip('No visits present in the test environment.')
    assert len(visit_summary.results) > 0


async def test_visit_detail(
    api_client: APIClient,
    visit_summary: VisitResponse,
):
    """Test getting the details of a visit"""
    for v_summary in visit_summary.results:
        v_detail = await api_client.visits.retrieve(v_summary.id)
        assert type(v_detail) is VisitDetail
        assert v_detail.id == v_summary.id
