""" A day category links a calendar to a schedule. 

The calendar determines the days of the year that fall into a day category, 
and the schedule determines what happens at certain times on those days.
"""

from typing import Optional

from ..utils import AppBaseModel, HrefMixin


class DayCategorySummary(
    AppBaseModel,
    HrefMixin,
):
    """Represents a single entry from the response"""

    name: str
    description: Optional[str]
    notes: Optional[str]
