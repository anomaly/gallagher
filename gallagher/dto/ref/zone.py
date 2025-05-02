from ..utils import (
    AppBaseModel,
    OptionalIdentityMixin,
    OptionalHrefMixin,
)


class AccessZoneRef(
    AppBaseModel,
    OptionalIdentityMixin,
    OptionalHrefMixin,
):
    """AccessZone represents"""

    name: str
