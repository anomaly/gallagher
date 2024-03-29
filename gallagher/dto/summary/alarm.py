from typing import Optional
from datetime import datetime

from ..utils import (
    AppBaseModel,
    HrefMixin,
    IdentityMixin,
)

from .event import (
    EventTypeSummary
)


class AlarmSourceSummary(
    AppBaseModel,
    HrefMixin,
    IdentityMixin,
):
    """ AlarmSource represents a device that has triggered an alarm
    """
    name: str


class AlarmZoneSummary(
    AppBaseModel,
    HrefMixin,
    IdentityMixin,
):
    """ #TODO: Revise this if it shows up in other places

    I have literally named this class to model the alarm_zones
    property in the access_group schema. I don't know if this
    is appropriate
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
    event: Optional[HrefMixin] = None
    note_presets: list[str] = []
    view: HrefMixin
    comment: HrefMixin
    acknowledge: Optional[HrefMixin] = None
    acknowledge_with_comment: Optional[HrefMixin] = None
    process: Optional[HrefMixin] = None
    process_with_comment: Optional[HrefMixin] = None
    force_process: Optional[HrefMixin] = None
