from gallagher.dto.utils import (
    AppBaseModel,
    HrefMixin,
)


class CardholderRef(
    AppBaseModel,
    HrefMixin,
):
    """ Reference to a Cardholder
    """
    name: str
