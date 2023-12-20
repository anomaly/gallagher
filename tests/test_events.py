

async def test_event_types():

    from gallagher.cc.alarms.events import (
        EventType
    )
    from gallagher.dto.response import (
        EventTypeResponse,
    )

    response = await EventType.list()
    assert type(response) is EventTypeResponse
