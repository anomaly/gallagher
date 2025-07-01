""" Test Receptions endpoints

"""

import pytest

from gallagher.dto.detail import ReceptionDetail
from gallagher.dto.response import ReceptionResponse
from gallagher.cc.receptions import Receptions


@pytest.fixture
async def reception_summary() -> ReceptionResponse:
    """Makes a single call to the reception list"""
    response = await Receptions.list()
    return response


async def test_reception_list(reception_summary: ReceptionResponse):
    """Test listing receptions"""
    assert type(reception_summary) is ReceptionResponse
    assert type(reception_summary.results) is list
    assert len(reception_summary.results) > 0


async def test_reception_detail(reception_summary: ReceptionResponse):
    """Test getting the details of a reception"""
    for r_summary in reception_summary.results:
        if not r_summary.id:
            pytest.skip(
                'Reception summary missing id, cannot retrieve detail.')
        r_detail = await Receptions.retrieve(r_summary.id)
        assert type(r_detail) is ReceptionDetail
        assert r_detail.id == r_summary.id
