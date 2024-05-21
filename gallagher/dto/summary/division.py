""" Division Summary

"""

from typing import Optional

from ..utils import (
    AppBaseModel,
    IdentityMixin,
    HrefMixin,
    OptionalHrefMixin,
)


class DivisionSummary(AppBaseModel, IdentityMixin, HrefMixin):
    """Division Summary

    Primarily separated for the cli to be able to distinguish between
    sumamry and detail responses, this is also very useful for the CLI
    """

    name: str
    description: Optional[str] = None
    server_display_name: Optional[str] = None
    parent: OptionalHrefMixin = None

    def __rich_repr__(self):
        return (
            self.id,
            self.name,
            self.server_display_name \
                if self.server_display_name \
                else "unavailable",
        )
