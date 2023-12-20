from ..utils import (
    AppBaseModel,
    HrefMixin
)


class AccessZoneRef(
    AppBaseModel,
    HrefMixin
):
    """ AccessZone represents
    """
    name: str
