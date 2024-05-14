""" Extra models that may be temporary

There are some models defined in the Gallagher API that seem to be 
placeholders for features to come in future version of command centre.
"""

from typing import Optional

from ..utils import (
    AppBaseModel,
    IdentityMixin,
)

class PlaceholderRef(
    AppBaseModel,
):
    """Placeholder Ref

    This is a placeholder for a reference to a future object
    """

    reserved: Optional[str] = "for future use"
