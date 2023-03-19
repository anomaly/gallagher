"""

"""

from typing import Optional
from .utils import AppBaseModel, HrefMixin

from .card_type import CardTypeDetail
# from .cardholder import CardholderSummary, CardholderDetail
# from .access_group import AccessGroupSummary, AccessGroupDetail
# from .role import RoleDetail

class Response(
    AppBaseModel
):
    """
    
    """
    next: Optional[HrefMixin]
    results: list[
        # CardholderSummary,
        # CardholderDetail,
        CardTypeDetail,
        # AccessGroupSummary,
        # AccessGroupDetail,
        # RoleDetail,
    ]
    
