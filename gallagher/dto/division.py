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
    DivisionRef,
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


class DivisionDetailResponse(
    AppBaseModel
):
    """ Division

    """

    results: list[DivisionDetail]
    next: Optional[HrefMixin] = None
