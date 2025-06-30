""" Test AccessGroups endpoints

"""

import pytest

from gallagher.dto.detail import AccessGroupDetail
from gallagher.dto.response import AccessGroupResponse
from gallagher.cc.access_groups import AccessGroups


@pytest.fixture
async def access_group_summary() -> AccessGroupResponse:
    """Makes a single call to the access group list"""
    response = await AccessGroups.list()
    return response


async def test_access_group_list(access_group_summary: AccessGroupResponse):
    """Test listing access groups"""
    assert type(access_group_summary) is AccessGroupResponse
    assert type(access_group_summary.results) is list
    assert len(access_group_summary.results) > 0


async def test_access_group_detail(access_group_summary: AccessGroupResponse):
    """Test getting the details of an access group"""
    for ag_summary in access_group_summary.results:
        ag_detail = await AccessGroups.retrieve(ag_summary.id)
        assert type(ag_detail) is AccessGroupDetail
        assert ag_detail.id == ag_summary.id
