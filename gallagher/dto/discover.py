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


class FeatureAccessGroupsRef(
    AppBaseModel,
):
    access_groups: Optional[OptionalHref] = OptionalHref()


class FeatureAccessZonesRef(
    AppBaseModel,
):
    access_zones: Optional[OptionalHref] = OptionalHref()


class FeatureAlarmZonesRef(
    AppBaseModel,
):
    alarm_zones: Optional[OptionalHref] = OptionalHref()


class FeatureAlarmsRef(
    AppBaseModel,
):
    alarms: Optional[OptionalHref] = OptionalHref()
    divisions: Optional[OptionalHref] = OptionalHref()
    updates: Optional[OptionalHref] = OptionalHref()


class FeatureCardTypesRef(
    AppBaseModel,
):
    assign: Optional[OptionalHref] = OptionalHref()
    card_types: Optional[OptionalHref] = OptionalHref()


class FeatureCardholdersRef(
    AppBaseModel,
):
    cardholders: Optional[OptionalHref] = OptionalHref()
    changes: Optional[OptionalHref] = OptionalHref()
    update_location_access_zones: Optional[OptionalHref] = OptionalHref()


class FeatureCompetenciesRef(
    AppBaseModel,
):
    competencies: Optional[OptionalHref] = OptionalHref()


class FeatureDayCategoriesRef(
    AppBaseModel,
):
    day_categories: Optional[OptionalHref] = OptionalHref()


class FeatureDivisionsRef(
    AppBaseModel,
):
    divisions: Optional[OptionalHref] = OptionalHref()


class FeatureDoorsRef(
    AppBaseModel,
):
    doors: Optional[OptionalHref] = OptionalHref()


class FeatureElevatorsRef(
    AppBaseModel,
):
    elevator_groups: Optional[OptionalHref] = OptionalHref()


class FeatureEventsRef(
    AppBaseModel,
):
    divisions: Optional[OptionalHref] = OptionalHref()
    event_groups: Optional[OptionalHref] = OptionalHref()
    events: Optional[OptionalHref] = OptionalHref()
    updates: Optional[OptionalHref] = OptionalHref()


class FeatureFenceZonesRef(
    AppBaseModel,
):
    fence_zones: Optional[OptionalHref] = OptionalHref()


class FeatureInputsRef(
    AppBaseModel,
):
    inputs: Optional[OptionalHref] = OptionalHref()


class FeatureInterlockGroupsRef(
    AppBaseModel,
):
    interlock_groups: Optional[OptionalHref] = OptionalHref()


class FeatureItemsRef(
    AppBaseModel,
):
    item_types: Optional[OptionalHref] = OptionalHref()
    items: Optional[OptionalHref] = OptionalHref()
    updates: Optional[OptionalHref] = OptionalHref()


class FeatureLockerBanksRef(
    AppBaseModel,
):
    locker_banks: Optional[OptionalHref] = OptionalHref()


class FeatureMacrosRef(
    AppBaseModel,
):
    macros: Optional[OptionalHref] = OptionalHref()


class FeatureOperatorGroupsRef(
    AppBaseModel,
):
    operator_groups: Optional[OptionalHref] = OptionalHref()


class FeatureOutputsRef(
    AppBaseModel,
):
    outputs: Optional[OptionalHref] = OptionalHref()


class FeaturePersonalDataFieldsRef(
    AppBaseModel,
):
    personal_data_fields: Optional[OptionalHref] = OptionalHref()


class FeatureReceptionsRef(
    AppBaseModel,
):
    receptions: Optional[OptionalHref] = OptionalHref()


class FeatureRolesRef(
    AppBaseModel,
):
    roles: Optional[OptionalHref] = OptionalHref()


class FeatureSchedulesRef(
    AppBaseModel,
):
    schedules: Optional[OptionalHref] = OptionalHref()


class FeatureVisitsRef(
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
    access_groups: Optional[FeatureAccessGroupsRef]\
        = FeatureAccessGroupsRef()
    access_zones: Optional[FeatureAccessZonesRef]\
        = FeatureAccessZonesRef()
    alarm_zones: Optional[FeatureAlarmZonesRef]\
        = FeatureAlarmZonesRef()
    alarms: Optional[FeatureAlarmsRef]\
        = FeatureAlarmsRef()
    card_types: Optional[FeatureCardTypesRef]\
        = FeatureCardTypesRef()
    cardholders: Optional[FeatureCardholdersRef]\
        = FeatureCardholdersRef()
    competencies: Optional[FeatureCompetenciesRef]\
        = FeatureCompetenciesRef()
    day_categories: Optional[FeatureDayCategoriesRef]\
        = FeatureDayCategoriesRef()
    divisions: Optional[FeatureDivisionsRef]\
        = FeatureDivisionsRef()
    doors: Optional[FeatureDoorsRef]\
        = FeatureDoorsRef()
    elevators: Optional[FeatureElevatorsRef]\
        = FeatureElevatorsRef()
    events: Optional[FeatureEventsRef]\
        = FeatureEventsRef()
    fence_zones: Optional[FeatureFenceZonesRef]\
        = FeatureFenceZonesRef()
    inputs: Optional[FeatureInputsRef]\
        = FeatureInputsRef()
    interlock_groups: Optional[FeatureInterlockGroupsRef]\
        = FeatureInterlockGroupsRef()
    items: Optional[FeatureItemsRef]\
        = FeatureItemsRef()
    locker_banks: Optional[FeatureLockerBanksRef]\
        = FeatureLockerBanksRef()
    macros: Optional[FeatureMacrosRef]\
        = FeatureMacrosRef()
    operator_groups: Optional[FeatureOperatorGroupsRef]\
        = FeatureOperatorGroupsRef()
    outputs: Optional[FeatureOutputsRef]\
        = FeatureOutputsRef()
    personal_data_fields: Optional[FeaturePersonalDataFieldsRef]\
        = FeaturePersonalDataFieldsRef()
    receptions: Optional[FeatureReceptionsRef]\
        = FeatureReceptionsRef()
    roles: Optional[FeatureRolesRef]\
        = FeatureRolesRef()
    schedules: Optional[FeatureSchedulesRef]\
        = FeatureSchedulesRef()
    visits: Optional[FeatureVisitsRef]\
        = FeatureVisitsRef()


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
