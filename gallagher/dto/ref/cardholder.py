from typing import Optional

from ..utils import (
    AppBaseModel,
    HrefMixin,
    IdentityMixin,
    OptionalHrefMixin,
)


class CardholderRef(
    AppBaseModel,
    HrefMixin,
):
    """Reference to a Cardholder"""

    name: str


class CardholderExtendedRef(
    AppBaseModel,
    IdentityMixin,
    OptionalHrefMixin,
):
    """Cardholder ref used with events

    Events seem to send partial information where href is missing at times
    (this is contrary to the documentation), name and id seem to always
    be present. This is likely because this is a summary
    """

    name: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
