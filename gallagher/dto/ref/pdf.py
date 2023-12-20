from gallagher.dto.utils import (
    AppBaseModel,
    HrefMixin,
)


class PDFRef(
    AppBaseModel,
    HrefMixin
):
    """ Personal Data Fields are custom fields for a card holder
    """
    name: str
