""" Test Interlock Group endpoints

"""

import pytest

from gallagher.cc import APIClient
from gallagher.dto.detail import InterlockGroupDetail
from gallagher.dto.response import InterlockGroupResponse
from gallagher.cc.interlock_groups import InterlockGroup


@pytest.fixture
async def interlock_group_summary(api_client: APIClient) -> InterlockGroupResponse:
    """Makes a single call to the interlock group list"""
    response = await api_client.interlock_groups.list()
    return response


async def test_interlock_group_list(interlock_group_summary: InterlockGroupResponse):
    """Test listing interlock groups"""
    assert type(interlock_group_summary) is InterlockGroupResponse
    assert type(interlock_group_summary.results) is list
    assert len(interlock_group_summary.results) > 0


async def test_interlock_group_detail(
    api_client: APIClient,
    interlock_group_summary: InterlockGroupResponse,
):
    """Test getting the details of an interlock group"""
    for ig_summary in interlock_group_summary.results:
        ig_detail = await api_client.interlock_groups.retrieve(ig_summary.id)
        assert type(ig_detail) is InterlockGroupDetail
        assert ig_detail.id == ig_summary.id
