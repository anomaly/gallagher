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
    """ """

    name: str
    description: Optional[str]
    parent: Optional[AccessGroupRef]
    division: IdentityMixin
    cardholders: OptionalHrefMixin
    server_display_name: Optional[str]

    description: Optional[str]
    parent: Optional[AccessGroupRef]
    division: DivisionDetail
    cardholders: OptionalHrefMixin
    server_display_name: Optional[str]
    children: list[AccessGroupRef]
    personal_data_definitions: list[PDFRef]

    visitor: bool
    escort_visitors: bool
    lock_unlock_access_zones: bool
    enter_during_lockdown: bool
    first_card_unlock: bool
    override_aperio_privacy: bool
    aperio_offline_access: bool
    disarm_alarm_zones: bool
    arm_alarm_zones: bool
    hvLf_fence_zones: bool
    view_alarms: bool
    shunt: bool
    lock_out_fence_zones: bool
    cancel_fence_zone_lockout: bool
    ack_all: bool
    ack_below_high: bool
    select_alarm_zone: bool
    arm_while_alarm: bool
    arm_while_active_alarm: bool
    isolate_alarm_zones: bool

    access: list[AccessSummary]
    salto_access: list[SaltoAccessItemSummary]
    alarm_zones: list[AlarmSummary]
