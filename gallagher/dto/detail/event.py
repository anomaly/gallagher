from typing import Optional
from datetime import datetime

from ..utils import (
    AppBaseModel,
    HrefMixin,
    IdentityMixin,
)

from ..ref import (
    AlarmRef,
    CardholderRef,
    DoorRef,
    AccessZoneRef,
    DivisionRef,
    ItemRef,
)


class EventDetail(
    AppBaseModel,
    HrefMixin,
    IdentityMixin,
):
    """Details of an event that took place on a server"""

    server_display_name: str
    time: datetime
    message: Optional[str]
    occurrences: int
    priority: int
    alarm: AlarmRef

    operator: CardholderRef
    source: ItemRef
    # group: EventGroupSummary
    # type: EventTypeSummary
    # event_type: EventTypeSummary
    # division: DivisionRef
    # cardholder: CardholderSummary
    entry_access_zone: AccessZoneRef
    exit_access_zone: AccessZoneRef
    door: DoorRef
    access_group: HrefMixin
    # card: str
    # modified_item: str
