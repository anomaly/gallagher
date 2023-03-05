
from typing import Optional

from .division import Division
from .utils import AppBaseModel, IdentityMixin, HrefMixin

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
    parent: Optional[AccessGroupSummary]
    division: Division
