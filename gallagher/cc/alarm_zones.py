""" Alarm Zones

"""

from gallagher.cc.core import APIEndpoint, EndpointConfig

from ..dto.detail import AlarmZoneDetail
from ..dto.response import AlarmZoneResponse


class AlarmZone(APIEndpoint):
    """Alarm Zones

    Provides access to alarm zone operations including listing
    and retrieving alarm zones. Alarm zones group items that
    raise alarms together for arming and disarming purposes.
    """

    def get_config(self) -> EndpointConfig:
        return EndpointConfig(
            endpoint=self._CAPABILITIES.features.alarm_zones.alarm_zones,
            dto_list=AlarmZoneResponse,
            dto_retrieve=AlarmZoneDetail,
        )
