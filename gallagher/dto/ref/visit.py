""" Visit Reference

"""

from typing import Optional
from datetime import datetime

from ..utils import AppBaseModel, HrefMixin


class VisitRef(
    AppBaseModel,
    HrefMixin
):
    """Visit Reference

    A reference to a visit containing minimal information
    for linking and identification purposes.
    """

    id: str
    visitor_name: str
    visit_date: Optional[datetime] = None
