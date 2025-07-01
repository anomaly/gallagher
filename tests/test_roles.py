""" Test Roles endpoints

"""

import pytest

from gallagher.dto.detail import RoleDetail
from gallagher.dto.response import RoleResponse
from gallagher.cc.roles import Roles


@pytest.fixture
async def role_summary() -> RoleResponse:
    """Makes a single call to the role list"""
    response = await Roles.list()
    return response


async def test_role_list(role_summary: RoleResponse):
    """Test listing roles"""
    assert type(role_summary) is RoleResponse
    assert type(role_summary.results) is list
    assert len(role_summary.results) > 0


async def test_role_detail(role_summary: RoleResponse):
    """Test getting the details of a role"""
    for r_summary in role_summary.results:
        if not r_summary.id:
            pytest.skip('Role summary missing id, cannot retrieve detail.')
        r_detail = await Roles.retrieve(r_summary.id)
        assert type(r_detail) is RoleDetail
        assert r_detail.id == r_summary.id
