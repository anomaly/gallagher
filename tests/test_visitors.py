""" Test Visitors endpoints

"""

import pytest

from gallagher.dto.detail import VisitorDetail
from gallagher.dto.response import VisitorResponse
from gallagher.cc.visitors import Visitors


@pytest.fixture
async def visitor_summary() -> VisitorResponse:
    """Makes a single call to the visitor list"""
    response = await Visitors.list()
    return response


async def test_visitor_list(visitor_summary: VisitorResponse):
    """Test listing visitors"""
    assert type(visitor_summary) is VisitorResponse
    assert type(visitor_summary.results) is list
    assert len(visitor_summary.results) > 0


async def test_visitor_detail(visitor_summary: VisitorResponse):
    """Test getting the details of a visitor"""
    for v_summary in visitor_summary.results:
        v_detail = await Visitors.retrieve(v_summary.id)
        assert type(v_detail) is VisitorDetail
        assert v_detail.id == v_summary.id
