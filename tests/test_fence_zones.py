""" Test Fence Zone endpoints

"""

import pytest

from gallagher.cc import APIClient
from gallagher.dto.detail import FenceZoneDetail
from gallagher.dto.response import FenceZoneResponse
from gallagher.cc.fence_zones import FenceZone


@pytest.fixture
async def fence_zone_summary(api_client: APIClient) -> FenceZoneResponse:
    """Makes a single call to the fence zone list"""
    response = await api_client.fence_zones.list()
    return response


async def test_fence_zone_list(fence_zone_summary: FenceZoneResponse):
    """Test listing fence zones"""
    assert type(fence_zone_summary) is FenceZoneResponse
    assert type(fence_zone_summary.results) is list
    assert len(fence_zone_summary.results) > 0


async def test_fence_zone_detail(
    api_client: APIClient,
    fence_zone_summary: FenceZoneResponse,
):
    """Test getting the details of a fence zone"""
    for fz_summary in fence_zone_summary.results:
        fz_detail = await api_client.fence_zones.retrieve(fz_summary.id)
        assert type(fz_detail) is FenceZoneDetail
        assert fz_detail.id == fz_summary.id
