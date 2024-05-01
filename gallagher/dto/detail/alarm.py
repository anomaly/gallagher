""" Alarm Details

The following are used to parse the details of an alarm

"""
from typing import Optional
from datetime import datetime

from ..utils import (
    AppBaseModel,
    HrefMixin,
    IdentityMixin,
)

from ..ref import (
	CardholderRef,
	OperatorRef,
	InstructionRef,
)

from ..summary import (
	EventTypeSummary,
    AlarmSourceSummary,
)

class AlarmHistoryDetail(
	AppBaseModel,
):
    """ Alarm History presented in the details
    """
    action: str
    time: datetime
    comment: str # Comment provided as part of an action
    operator: OperatorRef

class AlarmDetail(
    AppBaseModel,
    HrefMixin,
    IdentityMixin,
):
    """ AlarmSummary gives us unactioned events from the CC

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
    event: Optional[HrefMixin] = None
    note_presets: list[str] = []

    # The following URLS should be used to follow through
    # on various actions that the system allows
    view: HrefMixin
    comment: HrefMixin
    acknowledge: Optional[HrefMixin] = None
    acknowledge_with_comment: Optional[HrefMixin] = None
    process: Optional[HrefMixin] = None
    process_with_comment: Optional[HrefMixin] = None
    force_process: Optional[HrefMixin] = None

    # Details fields, these are what don't appear in the summary
    details: Optional[str] = ""
    history: Optional[list[AlarmHistoryDetail]] = []
    instruction: Optional[InstructionRef] = None
    cardholder: Optional[CardholderRef] = None
