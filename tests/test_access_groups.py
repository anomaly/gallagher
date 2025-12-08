""" Test AccessGroups endpoints

"""

import pytest

from gallagher.cc import APIClient
from gallagher.dto.detail import AccessGroupDetail
from gallagher.dto.response import AccessGroupResponse

@pytest.fixture
async def access_group_summary(api_client: APIClient) -> AccessGroupResponse:
    """Makes a single call to the access group list"""
    response = await api_client.access_groups.list()
    return response


async def test_access_group_list(access_group_summary: AccessGroupResponse):
    """Test listing access groups"""
    assert type(access_group_summary) is AccessGroupResponse
    assert type(access_group_summary.results) is list
    assert len(access_group_summary.results) > 0


# async def test_access_group_detail(
#         api_client: APIClient,
#         access_group_summary: AccessGroupResponse
#     ):
#     """Test getting the details of an access group"""
#     for ag_summary in access_group_summary.results:
#         if not ag_summary.id:
#             pytest.skip(
#                 'Access group summary missing id, cannot retrieve detail.')
#         ag_detail = await api_client.access_groups.retrieve(ag_summary.id)
#         assert type(ag_detail) is AccessGroupDetail
#         assert ag_detail.id == ag_summary.id
