""" Test Zones endpoints

"""

import pytest

from gallagher.cc import APIClient

from gallagher.dto.detail import ZoneDetail
from gallagher.dto.response import ZoneResponse
from gallagher.cc.zones import Zone


@pytest.fixture
async def zone_summary(api_client: APIClient) -> ZoneResponse:
    """Makes a single call to the zone list"""
    response = await api_client.zones.list()
    return response


async def test_zone_list(zone_summary: ZoneResponse):
    """Test listing zones"""
    assert type(zone_summary) is ZoneResponse
    assert type(zone_summary.results) is list
    assert len(zone_summary.results) > 0


async def test_zone_detail(
    api_client: APIClient,
    zone_summary: ZoneResponse,
):
    """Test getting the details of a zone"""
    for z_summary in zone_summary.results:
        z_detail = await api_client.zones.retrieve(z_summary.id)
        assert type(z_detail) is ZoneDetail
        assert z_detail.id == z_summary.id
