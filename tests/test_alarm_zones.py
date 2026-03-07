""" Test Alarm Zone endpoints

"""

import pytest

from gallagher.cc import APIClient
from gallagher.dto.detail import AlarmZoneDetail
from gallagher.dto.response import AlarmZoneResponse
from gallagher.cc.alarm_zones import AlarmZone


@pytest.fixture
async def alarm_zone_summary(api_client: APIClient) -> AlarmZoneResponse:
    """Makes a single call to the alarm zone list"""
    response = await api_client.alarm_zones.list()
    return response


async def test_alarm_zone_list(alarm_zone_summary: AlarmZoneResponse):
    """Test listing alarm zones"""
    assert type(alarm_zone_summary) is AlarmZoneResponse
    assert type(alarm_zone_summary.results) is list
    assert len(alarm_zone_summary.results) > 0


async def test_alarm_zone_detail(
    api_client: APIClient,
    alarm_zone_summary: AlarmZoneResponse,
):
    """Test getting the details of an alarm zone"""
    for az_summary in alarm_zone_summary.results:
        az_detail = await api_client.alarm_zones.retrieve(az_summary.id)
        assert type(az_detail) is AlarmZoneDetail
        assert az_detail.id == az_summary.id
