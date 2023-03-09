"""

"""

from typing import Optional

from .utils import AppBaseModel,\
    IdentityMixin, HrefMixin

from .access_group import AccessGroupRef,\
    AccessGroupSummary

class VisitorType(
    AppBaseModel,
    IdentityMixin
):
    """
    """
    access_group : AccessGroupRef
    host_access_groups: list[AccessGroupSummary]
    visitor_access_groups: list[AccessGroupSummary]

class VisitorManagement(
    AppBaseModel
):
    """
    """
    active: bool
    visitor_types: list[VisitorType]
    
class Division(
    AppBaseModel,
    IdentityMixin,
):
    """
    """

    name: str
    description: Optional[str]
    server_display_name: str
    parent: Optional[HrefMixin]

    visitor_management: VisitorManagement
