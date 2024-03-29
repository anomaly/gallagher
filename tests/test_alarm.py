""" Alarms are raised by the command centre, we want
to make sure that we are getting valid responses.

"""


async def test_alarms_list():
    """ Get a list of item types and iterates through it
    these are a summary response

    """
    from gallagher.cc.alarms import (
        Alarms
    )
    from gallagher.dto.response import (
        AlarmResponse
    )

    response = await Alarms.list()
    assert type(response) is AlarmResponse
    assert type(response.alarms) is list
    assert len(response.alarms) > 0
