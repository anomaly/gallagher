from typing import Optional

from ..utils import (
    AppBaseModel,
    IdentityMixin,
)


class EventGroupRef(
    AppBaseModel,
    IdentityMixin,
):
    """Event Group Reference

    This is a reference to an event group, it is used in the
    event type response.
    """

    name: str
