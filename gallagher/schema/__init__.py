"""

"""

from typing import Optional
from .utils import AppBaseModel, HrefMixin

from .cardholder import CardholderSummary, CardholderDetail

class Response(
    AppBaseModel
):
    next: Optional[HrefMixin]
    results: list[
        CardholderSummary,
        CardholderDetail
    ]
    
