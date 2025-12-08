""" Test Lockers endpoints

"""

import pytest

from gallagher.cc import APIClient

from gallagher.dto.detail import LockerDetail
from gallagher.dto.response import LockerResponse
from gallagher.cc.lockers import Lockers


@pytest.fixture
async def locker_summary(api_client: APIClient) -> LockerResponse:
    """Makes a single call to the locker list"""
    response = await api_client.lockers.list()
    return response


async def test_locker_list(locker_summary: LockerResponse):
    """Test listing lockers"""
    assert type(locker_summary) is LockerResponse
    assert type(locker_summary.results) is list
    if not locker_summary.results:
        pytest.skip('No lockers present in the test environment.')
    assert len(locker_summary.results) > 0


async def test_locker_detail(
    api_client: APIClient,
    locker_summary: LockerResponse,
):
    """Test getting the details of a locker"""
    for l_summary in locker_summary.results:
        l_detail = await api_client.lockers.retrieve(l_summary.id)
        assert type(l_detail) is LockerDetail
        assert l_detail.id == l_summary.id
