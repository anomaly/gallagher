""" Alarms are raised by the command centre, we want
to make sure that we are getting valid responses.

"""
from datetime import datetime

import pytest


from gallagher.dto.detail import (
    AlarmDetail,
)

from gallagher.dto.response import (
    AlarmSummaryResponse,
)

from gallagher.cc.alarms import (
    Alarms,
)

# Fixture for the comment, this will create a timestamp
# based string so we can compare this is a comment that
# was created for this test

@pytest.fixture
async def alarm_comment():
    return f"Test suite alarm comment {datetime.now()}"


@pytest.fixture
async def alarm_summary() -> AlarmSummaryResponse:
    """ Get a list of item types and iterates through it
    these are a summary response

    """
    response = await Alarms.list()
    return response

async def test_alarms_list(
    alarm_summary: AlarmSummaryResponse
):
    """ Get a list of item types and iterates through it
    these are a summary response

    """
    assert type(alarm_summary) is AlarmSummaryResponse
    assert type(alarm_summary.alarms) is list
    assert len(alarm_summary.alarms) > 0


async def test_alarms_detail(
    alarm_summary: AlarmSummaryResponse
):
    """ Get details of all the alarms 

    This will get the details of all the alarms and then
    compare the summary with the detail to make sure that
    the data is consistent.
    """

    for alarm_summary in alarm_summary.alarms:
        # Get the detail of the alarm for comparison
        alarm_detail_response = await Alarms.retrieve(
            alarm_summary.id
        )
        assert type(alarm_detail_response) is AlarmDetail
        assert (alarm_detail_response.id == alarm_summary.id)

async def test_alarms_post_comment(
    alarm_summary: AlarmSummaryResponse,
    alarm_comment: str
):
    """ Posts a commend to an alarm 

    This will make a new comment and then expect the next test
    to figure out that we have a new comment on the first
    """
    for alarm_summary in alarm_summary.alarms:
        # Get the detail of the alarm for comparison
        await Alarms.comment(
            alarm_summary,
            alarm_comment,
        )

async def test_alarms_comment_exists(
    alarm_summary: AlarmSummaryResponse,
    alarm_comment: str
):
    for alarm_summary in alarm_summary.alarms:

        # Get alarm detail to check the comment
        alarm_detail_response = await Alarms.retrieve(
            alarm_summary.id
        )

        for history in alarm_detail_response.history:
            # Find the comment in the history
            if history.comment == alarm_comment and \
                history.action == "comment":
                assert True
                return

