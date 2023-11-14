"""

"""
from typing import Optional

from .utils import (
    AppBaseModel,
    HrefMixin,
    IdentityMixin,
)


class EventType(
    AppBaseModel,
    IdentityMixin,
):
    name: str


class EventSummary(
    AppBaseModel,
    IdentityMixin,
    HrefMixin
):
    """ Events that the Command Centre generates

    """
    server_display_name: str
    time: str
    message: Optional[str]
    occurrences: int
    priority: int

    # Hrefs to follows other events
    next: HrefMixin
    previous: HrefMixin
    updates: HrefMixin
