"""


"""

def test_schedules_list():
    
    from gallagher.cc.alarms.schedule import Schedule
    from gallagher.schema.schedule import ScheduleSummaryResponse

    response = Schedule.list()
    assert type(response) is ScheduleSummaryResponse
    assert type(response.results) is list
    assert len(response.results) > 0

