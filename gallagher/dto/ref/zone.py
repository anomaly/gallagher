from ..utils import (
    AppBaseModel,
    OptionalIdentityMixin,
    HrefMixin,
)


class AccessZoneRef(
    AppBaseModel,
    OptionalIdentityMixin,
    HrefMixin
):
    """AccessZone represents"""

    name: str
