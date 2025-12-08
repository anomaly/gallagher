""" Test Roles endpoints

"""

import pytest

from gallagher.cc import APIClient

from gallagher.dto.detail import RoleDetail
from gallagher.dto.response import RoleResponse
from gallagher.cc.roles import Role


@pytest.fixture
async def role_summary(api_client: APIClient) -> RoleResponse:
    """Makes a single call to the role list"""
    response = await api_client.roles.list()
    return response


async def test_role_list(role_summary: RoleResponse):
    """Test listing roles"""
    assert type(role_summary) is RoleResponse
    assert type(role_summary.results) is list
    assert len(role_summary.results) > 0


async def test_role_detail(
    api_client: APIClient,
    role_summary: RoleResponse,
):
    """Test getting the details of a role"""
    for r_summary in role_summary.results:
        if not r_summary.id:
            pytest.skip('Role summary missing id, cannot retrieve detail.')
        r_detail = await api_client.roles.retrieve(r_summary.id)
        assert type(r_detail) is RoleDetail
        assert r_detail.id == r_summary.id
