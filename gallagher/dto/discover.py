""" Command Centre API discovery

The Command Centre API has a discovery endpoint that allows

"""

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
    access_groups: FeatureAccessGroups
    access_zones: FeatureAccessZones
    alarm_zones: FeatureAlarmZones
    alarms: FeatureAlarms
    card_types: FeatureCardTypes
    cardholders: FeatureCardholders
    competencies: FeatureCompetencies
    day_categories: FeatureDayCategories
    divisions: FeatureDivisions
    doors: FeatureDoors
    elevators: FeatureElevators
    events: FeatureEvents
    fence_zones: FeatureFenceZones
    inputs: FeatureInputs
    interlock_groups: FeatureInterlockGroups
    items: FeatureItems
    locker_banks: FeatureLockerBanks
    macros: FeatureMacros
    operator_groups: FeatureOperatorGroups
    outputs: FeatureOutputs
    personal_data_fields: FeaturePersonalDataFields
    receptions: FeatureReceptions
    roles: FeatureRoles
    schedules: FeatureSchedules
    visits: FeatureVisits


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
