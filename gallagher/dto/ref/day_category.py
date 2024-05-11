""" A day category links a calendar to a schedule. 

The calendar determines the days of the year that fall into a day category, 
and the schedule determines what happens at certain times on those days.
"""

from ..utils import AppBaseModel, HrefMixin


class DayCategoryRef(
    AppBaseModel,
    HrefMixin,
):
    """A reference to a day category

    This is what is sent by the day_category endpoint as of v9
    the references can be used from other endpoints.
    """

    name: str
