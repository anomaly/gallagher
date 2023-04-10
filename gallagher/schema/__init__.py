"""

 Resources:
  - https://bit.ly/3UkhQhS
  
"""

from typing import Optional, Union, Annotated
from pydantic import Field

from .utils import AppBaseModel, HrefMixin

from .card_type import CardTypeDetail
from .division import DivisionDetail
from .items import ItemSummary, ItemTypeDetail
# from .cardholder import CardholderSummary, CardholderDetail
# from .access_group import AccessGroupSummary, AccessGroupDetail
# from .role import RoleDetail

ResultItems = Annotated[
    Union[
        CardTypeDetail,
        DivisionDetail,
        ItemSummary,
        ItemTypeDetail,
    ],
    Field
]

class Response(
    AppBaseModel
):
    """
    
    """
    next: Optional[HrefMixin]
    results: list[ResultItems]
    
