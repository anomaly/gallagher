""" Test Doors endpoints

"""

import pytest

from gallagher.dto.detail import DoorDetail
from gallagher.dto.response import DoorResponse
from gallagher.cc.doors import Doors


@pytest.fixture
async def door_summary() -> DoorResponse:
    """Makes a single call to the door list"""
    response = await Doors.list()
    return response


async def test_door_list(door_summary: DoorResponse):
    """Test listing doors"""
    assert type(door_summary) is DoorResponse
    assert type(door_summary.results) is list
    assert len(door_summary.results) > 0


async def test_door_detail(door_summary: DoorResponse):
    """Test getting the details of a door"""
    for d_summary in door_summary.results:
        d_detail = await Doors.retrieve(d_summary.id)
        assert type(d_detail) is DoorDetail
        assert d_detail.id == d_summary.id
