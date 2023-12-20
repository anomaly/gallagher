from typing import Optional

from ..utils import (
    AppBaseModel,
    IdentityMixin,
)


class EventTypeSummary(
    AppBaseModel,
    IdentityMixin,
):
    """ An event type has identifiers and names
    """
    name: str
