from typing import Optional

from gallagher.dto.utils import (
    AppBaseModel,
    IdentityMixin,
    HrefMixin
)


class DivisionDetail(
    AppBaseModel,
    IdentityMixin,
    HrefMixin
):
    """
    """

    name: str
    description: Optional[str] = None
    server_display_name: Optional[str] = None
    parent: Optional[HrefMixin] = None

    # TODO: Looks like we don't have access to visitor management
    # on our test instance at the moment
    # visitor_management: visitor.VisitorManagementSummary
