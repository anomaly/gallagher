from ..utils import (
    AppBaseModel,
    HrefMixin,
)


class AlarmRef(AppBaseModel, HrefMixin):
    """AlarmRef represents a single alarm"""

    state: str


class AlarmZoneRef(AppBaseModel, HrefMixin):
    """AccessZone represents"""

    name: str
