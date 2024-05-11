""" Schedule lists
"""

import pytest

from gallagher.dto.response import (
    ScheduleSummaryResponse,
)

from gallagher.cc.alarms.schedule import Schedule


@pytest.fixture
async def schedule_summary_response() -> ScheduleSummaryResponse:
    """Makes a single call to the schedule list

    This is passed as a fixture to all other calls around
    on this test to save network round trips.

    :return: ScheduleSummaryResponse
    """

    response = await Schedule.list()
    return response


async def test_schedules_list(schedule_summary_response: ScheduleSummaryResponse):
    """Tests the schedule list

    :param schedule_summary_response: ScheduleSummaryResponse
    """
    assert type(schedule_summary_response) is ScheduleSummaryResponse
    assert type(schedule_summary_response.results) is list
    assert len(schedule_summary_response.results) > 0
