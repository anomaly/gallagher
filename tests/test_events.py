""" Events

"""

import pytest
import asyncio

from gallagher.dto.response import (
    EventTypeResponse,
    EventSummaryResponse,
)

from gallagher.dto.summary.event import (
    EventSummary,
)

from gallagher.cc.alarms.events import (
    EventType,
    Event,
    EventGroups,
)


@pytest.fixture
async def event_types() -> EventTypeResponse:
    """Fetch the Event Types list from CC"""
    response = await EventType.list()
    return response


@pytest.fixture
async def event_summary() -> EventSummaryResponse:
    """Fetch a list of Events from the CC"""
    response = await Event.list()    
    return response


async def test_event_types(event_types: EventTypeResponse):
    """Tests the Event Listing Resposne type"""
    assert type(event_types) is EventTypeResponse


async def test_event_summary(event_summary: EventSummaryResponse):
    """Test the event summary response type"""
    assert type(event_summary) is EventSummaryResponse


async def test_event_groups():
    """Get a list of Event Groups 
    
    These will be used by other endpoints to filter events
    """
    response = await EventGroups.list()
    assert type(response) is EventTypeResponse
    assert len(response.event_groups) > 0


async def test_event_updates():
    """ Test polling events from the Command Centre
    
    - Run around 10 loops and then quit
    - Don't do this via a fixture as we need to poll
    """

    # Make an asyncio Event, this is used to signal the event to stop
    # use this to cancel the loop
    event = asyncio.Event()
    event.set()
    count = 0

    async for updates in Event.follow(
        asyncio_event=event,
    ):
        for update_event in updates.events:
            assert type(update_event) is EventSummary
            count += 1
            if count > 3:
                event.clear()
                break
