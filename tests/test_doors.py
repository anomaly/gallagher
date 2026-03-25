""" Test Doors endpoints

"""

import pytest

from gallagher.cc import APIClient

from gallagher.dto.detail import DoorDetail
from gallagher.dto.response import DoorResponse
from gallagher.cc.doors import Door


@pytest.fixture
async def door_summary(api_client: APIClient) -> DoorResponse:
    """Makes a single call to the door list"""
    response = await api_client.doors.list()
    return response


async def test_door_list(door_summary: DoorResponse):
    """Test listing doors"""
    assert type(door_summary) is DoorResponse
    assert type(door_summary.results) is list
    assert len(door_summary.results) > 0


async def test_door_detail(
        api_client: APIClient,
        door_summary: DoorResponse,
):
    """Test getting the details of a door"""
    for d_summary in door_summary.results:
        d_detail = await api_client.doors.retrieve(d_summary.id)
        assert type(d_detail) is DoorDetail
        assert d_detail.id == d_summary.id
