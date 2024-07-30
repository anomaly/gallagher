from typing import Optional
from datetime import datetime

from ..utils import (
    AppBaseModel,
    HrefMixin,
    OptionalHrefMixin,
    IdentityMixin,
)

from .event import EventTypeSummary


class AlarmSourceSummary(
    AppBaseModel,
    HrefMixin,
    IdentityMixin,
):
    """AlarmSource represents a device that has triggered an alarm"""

    name: str


class AlarmSummary(
    AppBaseModel,
    HrefMixin,
    IdentityMixin,
):
    """AlarmSummary gives us unactioned events from the CC

    While the detail and summary would typically differ, it seems that
    the API endpoints return more detail in the summary endpoints.

    Note: that we have a number of hrefs that we should follow to
    HATEOAS compliance as per the documentation.

    """

    time: datetime
    message: str
    source: AlarmSourceSummary
    type: str
    event_type: Optional[EventTypeSummary] = None
    priority: int
    state: str
    active: bool
    division: HrefMixin
    event: OptionalHrefMixin = None
    note_presets: list[str] = []

    # The following URLS should be used to follow through
    # on various actions that the system allows
    view: HrefMixin
    comment: HrefMixin
    acknowledge: OptionalHrefMixin = None
    acknowledge_with_comment: OptionalHrefMixin = None
    process: OptionalHrefMixin = None
    process_with_comment: OptionalHrefMixin = None
    force_process: OptionalHrefMixin = None

    def __rich_repr__(self):
        from gallagher.cli.const import SEVERITY_COLOURS
        return (
            self.id,
            f"[{SEVERITY_COLOURS[self.priority]}]{self.priority}",
            self.time.strftime('%c'),
            f"[{SEVERITY_COLOURS[self.priority]}]{self.type}",
        )

    def __str__(self):
        return f"{self.id} {self.priority} {self.type}"

