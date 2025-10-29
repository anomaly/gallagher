from ..utils import AppBaseModel, IdentityMixin, HrefMixin
from ..ref import AccessGroupRef, DivisionRef

from .access_group import (
    AccessGroupSummary,
)

from typing import Optional
from datetime import datetime


class VisitorTypeSummary(AppBaseModel, IdentityMixin):
    """Visitor Types are a combination of:
    - Access Group
    - Host Access Groups
    - Visitor Access Groups

    these are represented in Divisions
    """

    access_group: AccessGroupRef
    host_access_groups: list[AccessGroupSummary]
    visitor_access_groups: list[AccessGroupSummary]


class VisitorManagementSummary(AppBaseModel):
    """This is the summary of the Visitor Management that appears
    in Divisions.
    """

    active: bool
    visitor_types: list[VisitorTypeSummary]


class VisitorSummary(
    AppBaseModel,
    IdentityMixin,
    HrefMixin
):
    """Visitor Summary

    A summary view of a visitor containing key information
    for listing and basic operations.
    """

    first_name: str
    last_name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    division: Optional[DivisionRef] = None
    created: Optional[datetime] = None
    modified: Optional[datetime] = None
