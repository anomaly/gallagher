""" Test Elevator Group endpoints

"""

import pytest

from gallagher.cc import APIClient
from gallagher.dto.detail import ElevatorDetail
from gallagher.dto.response import ElevatorResponse
from gallagher.cc.elevators import Elevator


@pytest.fixture
async def elevator_summary(api_client: APIClient) -> ElevatorResponse:
    """Makes a single call to the elevator group list"""
    response = await api_client.elevators.list()
    return response


async def test_elevator_list(elevator_summary: ElevatorResponse):
    """Test listing elevator groups"""
    assert type(elevator_summary) is ElevatorResponse
    assert type(elevator_summary.results) is list
    assert len(elevator_summary.results) > 0


async def test_elevator_detail(
    api_client: APIClient,
    elevator_summary: ElevatorResponse,
):
    """Test getting the details of an elevator group"""
    for e_summary in elevator_summary.results:
        e_detail = await api_client.elevators.retrieve(e_summary.id)
        assert type(e_detail) is ElevatorDetail
        assert e_detail.id == e_summary.id
