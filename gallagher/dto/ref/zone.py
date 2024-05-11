from ..utils import (
    AppBaseModel,
    IdentityMixin,
    HrefMixin,
)


class AccessZoneRef(AppBaseModel, IdentityMixin, HrefMixin):
    """AccessZone represents"""

    name: str
