from .utils import (
    AppBaseModel,
    IdentityMixin
)

from ..ref import (
    AccessGroupRef
)

from ..summary import (
    AccessGroupSummary,
    VisitorTypeSummary,
)


class VisitorTypeSummary(
    AppBaseModel,
    IdentityMixin
):
    """ Visitor Types are a combination of:
    - Access Group
    - Host Access Groups
    - Visitor Access Groups

    these are represented in Divisions
    """
    access_group: AccessGroupRef
    host_access_groups: list[AccessGroupSummary]
    visitor_access_groups: list[AccessGroupSummary]


class VisitorManagementSummary(
    AppBaseModel
):
    """ This is the summary of the Visitor Management that appears
    in Divisions.
    """
    active: bool
    visitor_types: list[VisitorTypeSummary]
