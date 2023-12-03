""" Command Centre API discovery

The Command Centre API has a discovery endpoint that allows

"""

from typing import (
    Annotated,
    Optional,
)

from pydantic.dataclasses import (
    dataclass,
)

from .utils import (
    AppBaseModel,
    HrefMixin
)


class FeatureAccessGroups(
    AppBaseModel,
):
    access_groups: Optional[HrefMixin] = None


class FeatureAccessZones(
    AppBaseModel,
):
    access_zones: Optional[HrefMixin] = None


class FeatureAlarmZones(
    AppBaseModel,
):
    alarm_zones: Optional[HrefMixin] = None


class FeatureAlarms(
    AppBaseModel,
):
    alarms: Optional[HrefMixin] = None
    divisions: Optional[HrefMixin] = None
    updates: Optional[HrefMixin] = None


class FeatureCardTypes(
    AppBaseModel,
):
    assign: Optional[HrefMixin] = None
    card_types: Optional[HrefMixin] = None


class FeatureCardholders(
    AppBaseModel,
):
    cardholders: Optional[HrefMixin] = None
    changes: Optional[HrefMixin] = None
    update_location_access_zones: Optional[HrefMixin] = None


class FeatureCompetencies(
    AppBaseModel,
):
    competencies: Optional[HrefMixin] = None


class FeatureDayCategories(
    AppBaseModel,
):
    day_categories: Optional[HrefMixin] = None


class FeatureDivisions(
    AppBaseModel,
):
    divisions: Optional[HrefMixin] = None


class FeatureDoors(
    AppBaseModel,
):
    doors: Optional[HrefMixin] = None


class FeatureElevators(
    AppBaseModel,
):
    elevator_groups: Optional[HrefMixin] = None


class FeatureEvents(
    AppBaseModel,
):
    divisions: Optional[HrefMixin] = None
    event_groups: Optional[HrefMixin] = None
    events: Optional[HrefMixin] = None
    updates: Optional[HrefMixin] = None


class FeatureFenceZones(
    AppBaseModel,
):
    fence_zones: Optional[HrefMixin] = None


class FeatureInputs(
    AppBaseModel,
):
    inputs: Optional[HrefMixin] = None


class FeatureInterlockGroups(
    AppBaseModel,
):
    interlock_groups: Optional[HrefMixin] = None


class FeatureItems(
    AppBaseModel,
):
    item_types: Optional[HrefMixin] = None
    items: Optional[HrefMixin] = None
    updates: Optional[HrefMixin] = None


class FeatureLockerBanks(
    AppBaseModel,
):
    locker_banks: Optional[HrefMixin] = None


class FeatureMacros(
    AppBaseModel,
):
    macros: Optional[HrefMixin] = None


class FeatureOperatorGroups(
    AppBaseModel,
):
    operator_groups: Optional[HrefMixin] = None


class FeatureOutputs(
    AppBaseModel,
):
    outputs: Optional[HrefMixin] = None


class FeaturePersonalDataFields(
    AppBaseModel,
):
    personal_data_fields: Optional[HrefMixin] = None


class FeatureReceptions(
    AppBaseModel,
):
    receptions: Optional[HrefMixin] = None


class FeatureRoles(
    AppBaseModel,
):
    roles: Optional[HrefMixin] = None


class FeatureSchedules(
    AppBaseModel,
):
    schedules: Optional[HrefMixin] = None


class FeatureVisits(
    AppBaseModel,
):
    visits: Optional[HrefMixin] = None


@dataclass
class FeaturesDetail(
    AppBaseModel,
):
    """ A detailed list of features that are available on the server.

    All features are marked as Optional, which means that by default
    it's assumed that they are not available on the server. Upon discovery
    if a feature is enabled on the server then we receive a href which
    indicates to the client that the feature is available.

    If a feature is unavailable the API client will throw an exception.
    """
    # access_groups: Optional[FeatureAccessGroups]\
    #     = FeatureAccessGroups()
    # access_zones: Optional[FeatureAccessZones]\
    #     = FeatureAccessZones()
    # alarm_zones: Optional[FeatureAlarmZones]\
    #     = FeatureAlarmZones()
    alarms: Optional[FeatureAlarms]\
        = FeatureAlarms()
    # card_types: Optional[FeatureCardTypes]\
    #     = FeatureCardTypes()
    # cardholders: Optional[FeatureCardholders]\
    #     = FeatureCardholders()
    # competencies: Optional[FeatureCompetencies]\
    #     = FeatureCompetencies()
    # day_categories: Optional[FeatureDayCategories]\
    #     = FeatureDayCategories()
    # divisions: Optional[FeatureDivisions]\
    #     = FeatureDivisions()
    # doors: Optional[FeatureDoors]\
    #     = FeatureDoors()
    # elevators: Optional[FeatureElevators]\
    #     = FeatureElevators()
    # events: Optional[FeatureEvents]\
    #     = FeatureEvents()
    # fence_zones: Optional[FeatureFenceZones]\
    #     = FeatureFenceZones()
    # inputs: Optional[FeatureInputs]\
    #     = FeatureInputs()
    # interlock_groups: Optional[FeatureInterlockGroups]\
    #     = FeatureInterlockGroups()
    # items: Optional[FeatureItems]\
    #     = FeatureItems()
    # locker_banks: Optional[FeatureLockerBanks]\
    #     = FeatureLockerBanks()
    # macros: Optional[FeatureMacros]\
    #     = FeatureMacros()
    # operator_groups: Optional[FeatureOperatorGroups]\
    #     = FeatureOperatorGroups()
    # outputs: Optional[FeatureOutputs]\
    #     = FeatureOutputs()
    # personal_data_fields: Optional[FeaturePersonalDataFields]\
    #     = FeaturePersonalDataFields()
    # receptions: Optional[FeatureReceptions]\
    #     = FeatureReceptions()
    # roles: Optional[FeatureRoles]\
    #     = FeatureRoles()
    # schedules: Optional[FeatureSchedules]\
    #     = FeatureSchedules()
    # visits: Optional[FeatureVisits]\
    #     = FeatureVisits()


@dataclass
class DiscoveryResponse(
    AppBaseModel,
):
    """ A response that outlines the capability of the server

    Gallagher requires customers to license individual features, if they are
    the server will return a 403 HTTP code. The purpose of this model is to
    discover what features are available on the server.

    The response should be memoized as it is unlikely to change during individual
    sessions, they can however change over a period of time.

    This API client is updated to work with various versions of the server, the
    server responds with a version string that can be used to determine if
    the API client can work with the server.  
    """

    version: Annotated[str, "The version of the server"]
    features: Annotated[FeaturesDetail,
                        "A list of features available on the server"]

    @property
    def get_sem_ver(self):
        """ Get a SemVer tuple from the version string
        """
        return self.version.split(".")
