
from typing import Optional

from .utils import AppBaseModel, IdentityMixin,\
    HrefMixin
from .division import DivisionDetail
from .pdf import PDFRef
from .schedule import ScheduleRef
from .zone import AccessZoneRef
from .salto import SaltoAccessItemSummary
from .alarm import AlarmZoneSummary

class AccessSummary(
    AppBaseModel
):
    """ Access is zone paired with a schedule
    """
    access_zone: AccessZoneRef
    schedule: ScheduleRef


class AccessGroupRef(
    AppBaseModel,
    HrefMixin
):
    """ Access Groups is what a user is assigned to to provide access to doors
    """
    name: str

class AccessGroupSummary(
    AccessGroupRef
):
    """ AccessGroup Summary is what the API returns on searches

    This builds on the Ref class to add the summary fields and is
    extended by the Detail class to add the fully remainder of
    the fields
    """
    description: Optional[str]
    parent: Optional[AccessGroupRef]
    division: IdentityMixin
    cardholders: Optional[HrefMixin]
    server_display_name: Optional[str]

class AccessGroupDetail(
    AccessGroupSummary
):
    """
    """
    description: Optional[str]
    parent: Optional[AccessGroupRef]
    division: DivisionDetail
    cardholders: Optional[HrefMixin]
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
    alarm_zones: list[AlarmZoneSummary]
