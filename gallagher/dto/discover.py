""" Command Centre API discovery

The Command Centre API has a discovery endpoint that allows

"""

from typing import Optional

from .utils import (
    AppBaseModel,
    HrefMixin
)


class FeatureAccessGroups(
    AppBaseModel,
):
    access_groups: HrefMixin


class FeatureAccessZones(
    AppBaseModel,
):
    access_zones: HrefMixin


class FeatureAlarmZones(
    AppBaseModel,
):
    alarm_zones: HrefMixin


class FeatureAlarms(
    AppBaseModel,
):
    alarms: HrefMixin
    divisions: HrefMixin
    updates: HrefMixin


class FeatureCardTypes(
    AppBaseModel,
):
    assign: HrefMixin
    card_types: HrefMixin


class FeatureCardholders(
    AppBaseModel,
):
    cardholders: HrefMixin
    changes: HrefMixin
    update_location_access_zones: HrefMixin


class FeatureCompetencies(
    AppBaseModel,
):
    competencies: HrefMixin


class FeatureDayCategories(
    AppBaseModel,
):
    day_categories: HrefMixin


class FeatureDivisions(
    AppBaseModel,
):
    divisions: HrefMixin


class FeatureDoors(
    AppBaseModel,
):
    doors: HrefMixin


class FeatureElevators(
    AppBaseModel,
):
    elevator_groups: HrefMixin


class FeatureEvents(
    AppBaseModel,
):
    divisions: HrefMixin
    event_groups: HrefMixin
    events: HrefMixin
    updates: HrefMixin


class FeatureFenceZones(
    AppBaseModel,
):
    fence_zones: HrefMixin


class FeatureInputs(
    AppBaseModel,
):
    inputs: HrefMixin


class FeatureInterlockGroups(
    AppBaseModel,
):
    interlock_groups: HrefMixin


class FeatureItems(
    AppBaseModel,
):
    item_types: HrefMixin
    items: HrefMixin
    updates: HrefMixin


class FeatureLockerBanks(
    AppBaseModel,
):
    locker_banks: HrefMixin


class FeatureMacros(
    AppBaseModel,
):
    macros: HrefMixin


class FeatureOperatorGroups(
    AppBaseModel,
):
    operator_groups: HrefMixin


class FeatureOutputs(
    AppBaseModel,
):
    outputs: HrefMixin


class FeaturePersonalDataFields(
    AppBaseModel,
):
    personal_data_fields: HrefMixin


class FeatureReceptions(
    AppBaseModel,
):
    receptions: HrefMixin


class FeatureRoles(
    AppBaseModel,
):
    roles: HrefMixin


class FeatureSchedules(
    AppBaseModel,
):
    schedules: HrefMixin


class FeatureVisits(
    AppBaseModel,
):
    visits: HrefMixin


class FeaturesDetail(
    AppBaseModel,
):
    """ 

    """
    access_groups: Optional[FeatureAccessGroups] = None
    access_zones: Optional[FeatureAccessZones] = None
    alarm_zones: Optional[FeatureAlarmZones] = None
    alarms: Optional[FeatureAlarms] = None
    card_types: Optional[FeatureCardTypes] = None
    cardholders: Optional[FeatureCardholders] = None
    competencies: Optional[FeatureCompetencies] = None
    day_categories: Optional[FeatureDayCategories] = None
    divisions: Optional[FeatureDivisions] = None
    doors: Optional[FeatureDoors] = None
    elevators: Optional[FeatureElevators] = None
    events: Optional[FeatureEvents] = None
    fence_zones: Optional[FeatureFenceZones] = None
    inputs: Optional[FeatureInputs] = None
    interlock_groups: Optional[FeatureInterlockGroups] = None
    items: Optional[FeatureItems] = None
    locker_banks: Optional[FeatureLockerBanks] = None
    macros: Optional[FeatureMacros] = None
    operator_groups: Optional[FeatureOperatorGroups] = None
    outputs: Optional[FeatureOutputs] = None
    personal_data_fields: Optional[FeaturePersonalDataFields] = None
    receptions: Optional[FeatureReceptions] = None
    roles: Optional[FeatureRoles] = None
    schedules: Optional[FeatureSchedules] = None
    visits: Optional[FeatureVisits] = None


class DiscoveryResponse(
    AppBaseModel,
):
    """  
    """

    version: str
    features: FeaturesDetail

    @property
    def get_sem_ver(self):
        """ Get a SemVer tuple from the version string
        """
        return self.version.split(".")
