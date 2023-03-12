"""

"""

from typing import Optional
from .utils import AppBaseModel, HrefMixin

from .cardholder import CardholderSummary, CardholderDetail
from .access_group import AccessGroupSummary, AccessGroupDetail
from .role import RoleDetail

class Response(
    AppBaseModel
):
    """
    
    """
    next: Optional[HrefMixin]
    results: list[
        CardholderSummary,
        CardholderDetail,
        AccessGroupSummary,
        AccessGroupDetail,
        RoleDetail,
    ]
    
