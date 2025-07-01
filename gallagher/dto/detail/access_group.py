from typing import Optional

from ..utils import (
    AppBaseModel,
    IdentityMixin,
    HrefMixin,
    OptionalHrefMixin,
)
from ..summary import (
    AlarmSummary,
    AccessSummary,
    SaltoAccessItemSummary,
)
from ..ref import (
    AccessGroupRef,
    PDFRef,
)

from .division import DivisionDetail


class AccessGroupDetail(
    AppBaseModel,
    HrefMixin,
):
    """Access Group Detail

    A detailed view of an access group containing all information
    for comprehensive operations and management.
    """

    id: Optional[str] = None
    name: str
    description: Optional[str] = None
    parent: Optional[dict] = None
    division: Optional[dict] = None
    serverDisplayName: Optional[str] = None
    personalDataDefinitions: Optional[list] = None
    overrideAperioPrivacy: Optional[bool] = None
    aperioOfflineAccess: Optional[bool] = None
    hvlfFenceZones: Optional[list] = None
    access: Optional[list] = None
    saltoAccess: Optional[dict] = None
    alarmZones: Optional[list] = None
    cardholders: OptionalHrefMixin = None

    # Legacy field names for backward compatibility
    server_display_name: Optional[str] = None
    children: Optional[list] = None
    personal_data_definitions: Optional[list] = None

    # Boolean permissions - all optional as they may not be present
    visitor: Optional[bool] = None
    escort_visitors: Optional[bool] = None
    lock_unlock_access_zones: Optional[bool] = None
    enter_during_lockdown: Optional[bool] = None
    first_card_unlock: Optional[bool] = None
    disarm_alarm_zones: Optional[bool] = None
    arm_alarm_zones: Optional[bool] = None
    view_alarms: Optional[bool] = None
    shunt: Optional[bool] = None
    lock_out_fence_zones: Optional[bool] = None
    cancel_fence_zone_lockout: Optional[bool] = None
    ack_all: Optional[bool] = None
    ack_below_high: Optional[bool] = None
    select_alarm_zone: Optional[bool] = None
    arm_while_alarm: Optional[bool] = None
    arm_while_active_alarm: Optional[bool] = None
    isolate_alarm_zones: Optional[bool] = None

    # Legacy access fields - optional
    salto_access: Optional[list] = None
    alarm_zones: Optional[list] = None
