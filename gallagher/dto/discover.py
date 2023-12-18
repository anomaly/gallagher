""" Command Centre API discovery

The Command Centre API has a discovery endpoint that allows

"""

from typing import (
    Annotated,
    Optional,
)

from .utils import (
    AppBaseModel,
    OptionalHref,
)


class FeatureAccessGroups(
    AppBaseModel,
):
    access_groups: Optional[OptionalHref] = OptionalHref()


class FeatureAccessZones(
    AppBaseModel,
):
    access_zones: Optional[OptionalHref] = OptionalHref()


class FeatureAlarmZones(
    AppBaseModel,
):
    alarm_zones: Optional[OptionalHref] = OptionalHref()


class FeatureAlarms(
    AppBaseModel,
):
    alarms: Optional[OptionalHref] = OptionalHref()
    divisions: Optional[OptionalHref] = OptionalHref()
    updates: Optional[OptionalHref] = OptionalHref()


class FeatureCardTypes(
    AppBaseModel,
):
    assign: Optional[OptionalHref] = OptionalHref()
    card_types: Optional[OptionalHref] = OptionalHref()


class FeatureCardholders(
    AppBaseModel,
):
    cardholders: Optional[OptionalHref] = OptionalHref()
    changes: Optional[OptionalHref] = OptionalHref()
    update_location_access_zones: Optional[OptionalHref] = OptionalHref()


class FeatureCompetencies(
    AppBaseModel,
):
    competencies: Optional[OptionalHref] = OptionalHref()


class FeatureDayCategories(
    AppBaseModel,
):
    day_categories: Optional[OptionalHref] = OptionalHref()


class FeatureDivisions(
    AppBaseModel,
):
    divisions: Optional[OptionalHref] = OptionalHref()


class FeatureDoors(
    AppBaseModel,
):
    doors: Optional[OptionalHref] = OptionalHref()


class FeatureElevators(
    AppBaseModel,
):
    elevator_groups: Optional[OptionalHref] = OptionalHref()


class FeatureEvents(
    AppBaseModel,
):
    divisions: Optional[OptionalHref] = OptionalHref()
    event_groups: Optional[OptionalHref] = OptionalHref()
    events: Optional[OptionalHref] = OptionalHref()
    updates: Optional[OptionalHref] = OptionalHref()


class FeatureFenceZones(
    AppBaseModel,
):
    fence_zones: Optional[OptionalHref] = OptionalHref()


class FeatureInputs(
    AppBaseModel,
):
    inputs: Optional[OptionalHref] = OptionalHref()


class FeatureInterlockGroups(
    AppBaseModel,
):
    interlock_groups: Optional[OptionalHref] = OptionalHref()


class FeatureItems(
    AppBaseModel,
):
    item_types: Optional[OptionalHref] = OptionalHref()
    items: Optional[OptionalHref] = OptionalHref()
    updates: Optional[OptionalHref] = OptionalHref()


class FeatureLockerBanks(
    AppBaseModel,
):
    locker_banks: Optional[OptionalHref] = OptionalHref()


class FeatureMacros(
    AppBaseModel,
):
    macros: Optional[OptionalHref] = OptionalHref()


class FeatureOperatorGroups(
    AppBaseModel,
):
    operator_groups: Optional[OptionalHref] = OptionalHref()


class FeatureOutputs(
    AppBaseModel,
):
    outputs: Optional[OptionalHref] = OptionalHref()


class FeaturePersonalDataFields(
    AppBaseModel,
):
    personal_data_fields: Optional[OptionalHref] = OptionalHref()


class FeatureReceptions(
    AppBaseModel,
):
    receptions: Optional[OptionalHref] = OptionalHref()


class FeatureRoles(
    AppBaseModel,
):
    roles: Optional[OptionalHref] = OptionalHref()


class FeatureSchedules(
    AppBaseModel,
):
    schedules: Optional[OptionalHref] = OptionalHref()


class FeatureVisits(
    AppBaseModel,
):
    visits: Optional[OptionalHref] = OptionalHref()


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
    access_groups: Optional[FeatureAccessGroups]\
        = FeatureAccessGroups()
    access_zones: Optional[FeatureAccessZones]\
        = FeatureAccessZones()
    alarm_zones: Optional[FeatureAlarmZones]\
        = FeatureAlarmZones()
    alarms: Optional[FeatureAlarms]\
        = FeatureAlarms()
    card_types: Optional[FeatureCardTypes]\
        = FeatureCardTypes()
    cardholders: Optional[FeatureCardholders]\
        = FeatureCardholders()
    competencies: Optional[FeatureCompetencies]\
        = FeatureCompetencies()
    day_categories: Optional[FeatureDayCategories]\
        = FeatureDayCategories()
    divisions: Optional[FeatureDivisions]\
        = FeatureDivisions()
    doors: Optional[FeatureDoors]\
        = FeatureDoors()
    elevators: Optional[FeatureElevators]\
        = FeatureElevators()
    events: Optional[FeatureEvents]\
        = FeatureEvents()
    fence_zones: Optional[FeatureFenceZones]\
        = FeatureFenceZones()
    inputs: Optional[FeatureInputs]\
        = FeatureInputs()
    interlock_groups: Optional[FeatureInterlockGroups]\
        = FeatureInterlockGroups()
    items: Optional[FeatureItems]\
        = FeatureItems()
    locker_banks: Optional[FeatureLockerBanks]\
        = FeatureLockerBanks()
    macros: Optional[FeatureMacros]\
        = FeatureMacros()
    operator_groups: Optional[FeatureOperatorGroups]\
        = FeatureOperatorGroups()
    outputs: Optional[FeatureOutputs]\
        = FeatureOutputs()
    personal_data_fields: Optional[FeaturePersonalDataFields]\
        = FeaturePersonalDataFields()
    receptions: Optional[FeatureReceptions]\
        = FeatureReceptions()
    roles: Optional[FeatureRoles]\
        = FeatureRoles()
    schedules: Optional[FeatureSchedules]\
        = FeatureSchedules()
    visits: Optional[FeatureVisits]\
        = FeatureVisits()


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

    version: Annotated[str, "The version of the server"] = "0.0.0"
    features: Annotated[FeaturesDetail,
                        "A list of features available on the server"
                        ] = FeaturesDetail()

    @property
    async def get_sem_ver(self):
        """ Get a SemVer tuple from the version string
        """
        return self.version.split(".")
