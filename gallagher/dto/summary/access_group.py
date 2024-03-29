from typing import Optional

from ..utils import (
    AppBaseModel,
    IdentityMixin,
    HrefMixin
)

from ..ref import (
    AccessGroupRef,
    AccessZoneRef,
    ScheduleRef,
)


class AccessSummary(
    AppBaseModel,
    HrefMixin,
):
    """ Access is zone paired with a schedule
    """
    access_zone: AccessZoneRef
    schedule: ScheduleRef


class AccessGroupSummary(
    AppBaseModel,
):
    """ AccessGroup Summary is what the API returns on searches

    This builds on the Ref class to add the summary fields and is
    extended by the Detail class to add the fully remainder of
    the fields
    """
    name: str
    description: Optional[str]
    parent: Optional[AccessGroupRef]
    division: IdentityMixin
    cardholders: Optional[HrefMixin]
    server_display_name: Optional[str]
