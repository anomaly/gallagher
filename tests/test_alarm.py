""" Alarms are raised by the command centre, we want
to make sure that we are getting valid responses.

"""


async def test_alarms_list():
    """ Get a list of item types and iterates through it
    these are a summary response

    """
    from gallagher.cc.alarms import (
        Alarms,
    )
    from gallagher.dto.response import (
        AlarmSummaryResponse,
    )

    response = await Alarms.list()
    assert type(response) is AlarmSummaryResponse
    assert type(response.alarms) is list
    assert len(response.alarms) > 0


async def test_alarms_detail():
    """ Get a list of alarms and then try and get it's detail
    """
    from gallagher.cc.alarms import (
        Alarms
    )

    from gallagher.dto.response import (
        AlarmSummaryResponse,
    )

    from gallagher.dto.detail import (
        AlarmDetail,
    )

    response = await Alarms.list()
    assert type(response) is AlarmSummaryResponse
    assert type(response.alarms) is list
    assert len(response.alarms) > 0

    for alarm_summary in response.alarms:
        # Get the detail of the alarm for comparison
        alarm_detail_response = await Alarms.retrieve(
            alarm_summary.id
        )
        assert type(alarm_detail_response) is AlarmDetail
        assert (alarm_detail_response.id == alarm_summary.id)


async def test_alarms_post_comment():
    """ Get a list of alarms and then try and get it's detail
    """
    from gallagher.cc.alarms import (
        Alarms
    )

    from gallagher.dto.response import (
        AlarmSummaryResponse,
    )

    from gallagher.dto.detail import (
        AlarmDetail,
    )

    response = await Alarms.list()
    assert type(response) is AlarmSummaryResponse
    assert type(response.alarms) is list
    assert len(response.alarms) > 0


    for alarm_summary in response.alarms:
        # Get the detail of the alarm for comparison
        created_status = await Alarms.comment(
            alarm_summary,
            "Statis comment"
        )

        assert(created_status == True)

