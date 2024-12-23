""" Events

"""

import pytest

from gallagher.dto.response import (
    EventTypeResponse,
    EventSummaryResponse,
)

from gallagher.cc.alarms.events import (
    EventType,
    Event,
    EventGroups,
)


@pytest.fixture
async def event_types() -> EventTypeResponse:
    """Event Types list"""
    response = await EventType.list()
    return response


@pytest.fixture
async def event_summary() -> EventSummaryResponse:
    """Event Summary list"""
    response = await Event.list()
    return response


async def test_event_types(event_types: EventTypeResponse):
    """Event Type listings"""
    assert type(event_types) is EventTypeResponse


async def test_event_summary(event_summary: EventSummaryResponse):
    """Event Summary listing"""
    assert type(event_summary) is EventSummaryResponse


async def test_event_groups():
    """Get a list of Event Groups 
    
    These will be used by other endpoints to filter events
    """
    response = await EventGroups.list()
    assert type(response) is EventTypeResponse
    assert len(response.event_groups) > 0
