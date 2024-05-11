""" Day Categories

"""

import pytest

from gallagher.dto.response import DayCategoryResponse

from gallagher.cc.alarms.day_category import DayCategory


@pytest.fixture
async def day_category() -> DayCategoryResponse:
    """Makes a single call to the day category list

    This is passed as a fixture to all other calls around
    on this test to save network round trips.

    :return: DayCategoryResponse
    """

    response = await DayCategory.list()
    return response


async def test_day_category(day_category: DayCategoryResponse):
    """Test listing a day category"""

    assert type(day_category) is DayCategoryResponse
    assert type(day_category.results) is list
    assert len(day_category.results) > 0
