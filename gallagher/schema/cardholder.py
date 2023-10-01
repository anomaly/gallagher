"""

"""

from datetime import datetime

from .utils import (
    AppBaseModel,
    IdentityMixin,
)


class CardholderSummary(
    AppBaseModel,
    IdentityMixin
):
    """
    The cardholder search at /api/cardholders returns an array of these. 
    It is a subset of what you get from a cardholder's detail page at 
    /api/cardholders/{id} 
    
    (linked as the href in this object), to be more suitable for large result sets.
    """
    
    first_name: str
    last_name: str
    short_name: str
    description: str
    authorised: str


class CardholderDetail(
    CardholderSummary
):
    """
    
    """
    last_successful_access_time: datetime
