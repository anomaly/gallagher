from typing import Optional

from ..utils import (
    AppBaseModel,
    IdentityMixin,
    HrefMixin,
    OptionalHrefMixin,
)


class DivisionDetail(AppBaseModel, IdentityMixin, HrefMixin):
    """ """

    name: str
    description: Optional[str] = None
    server_display_name: Optional[str] = None
    parent: OptionalHrefMixin = None

    # TODO: Looks like we don't have access to visitor management
    # on our test instance at the moment
    # visitor_management: visitor.VisitorManagementSummary

    def __rich_repr__(self):
        return (
            self.id,
            self.name,
            self.server_display_name \
                if self.server_display_name \
                    else "unavailable",
        )
