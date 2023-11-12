""" A day category links a calendar to a schedule. 

The calendar determines the days of the year that fall into a day category, 
and the schedule determines what happens at certain times on those days.
"""
from typing import Optional

from .utils import (
    AppBaseModel,
    HrefMixin
)


class DayCategoryRef(
    AppBaseModel,
    HrefMixin,
):
    """ A reference to a day category

    This is what is sent by the day_category endpoint as of v9
    the references can be used from other endpoints.
    """

    name: str


class DayCategory(
    DayCategoryRef,
):
    """ Represents a single entry from the response
    """

    name: str
    description: Optional[str]
    notes: Optional[str]


class DayCategoryResponse(
    AppBaseModel,
):
    """ The response has a list of results and a link to the next page
    """

    results: list[DayCategoryRef]
    next: Optional[HrefMixin] = None
