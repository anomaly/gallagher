"""

"""

from typing import Optional

from .utils import (
    AppBaseModel,
    IdentityMixin,
    HrefMixin
)

# import visitor.VisitorManagementSummary

class DivisionRef(
    AppBaseModel,
    IdentityMixin,
    HrefMixin
):
    """ Division reference is used to link to a division

    The Mixins cover all the fields that are returned in the
    summary, hence nothing has to be declared in the body
    """
    pass

    
class DivisionDetail(
    AppBaseModel,
    IdentityMixin,
):
    """
    """

    name: str
    description: Optional[str]
    server_display_name: Optional[str]
    parent: Optional[HrefMixin]

    # visitor_management: visitor.VisitorManagementSummary
