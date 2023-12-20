from typing import Optional

from ..utils import (
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
    short_name: Optional[str] = None
    description: Optional[str] = None
    authorised: bool

    def __rich_repr__(self):
        return [
            self.id,
            self.first_name,
            self.last_name,
            "yes" if self.authorised else "no"
        ]

    def __str__(self):
        return f"{self.id} {self.first_name} {self.last_name}"
