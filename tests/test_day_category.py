""" Day Categories

"""


async def test_day_category():

    from gallagher.cc.alarms.day_category import DayCategory
    from gallagher.dto.day_category import DayCategoryResponse

    response = await DayCategory.list()
    assert type(response) is DayCategoryResponse
    assert type(response.results) is list
    assert len(response.results) > 0
