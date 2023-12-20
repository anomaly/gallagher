from typing import Optional

from gallagher.dto.utils import (
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
