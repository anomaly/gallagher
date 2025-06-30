""" Test Visits endpoints

"""

import pytest

from gallagher.dto.detail import VisitDetail
from gallagher.dto.response import VisitResponse
from gallagher.cc.visits import Visits


@pytest.fixture
async def visit_summary() -> VisitResponse:
    """Makes a single call to the visit list"""
    response = await Visits.list()
    return response


async def test_visit_list(visit_summary: VisitResponse):
    """Test listing visits"""
    assert type(visit_summary) is VisitResponse
    assert type(visit_summary.results) is list
    assert len(visit_summary.results) > 0


async def test_visit_detail(visit_summary: VisitResponse):
    """Test getting the details of a visit"""
    for v_summary in visit_summary.results:
        v_detail = await Visits.retrieve(v_summary.id)
        assert type(v_detail) is VisitDetail
        assert v_detail.id == v_summary.id
