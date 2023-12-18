"""


"""


async def test_schedules_list():

    from gallagher.cc.alarms.schedule import Schedule
    from gallagher.dto.schedule import ScheduleSummaryResponse

    response = await Schedule.list()
    assert type(response) is ScheduleSummaryResponse
    assert type(response.results) is list
    assert len(response.results) > 0
