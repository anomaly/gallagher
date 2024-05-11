from typing import Optional

from ..utils import (
    AppBaseModel,
)

from ..ref import (
    FeatureAccessGroupsRef,
    FeatureAccessZonesRef,
    FeatureAlarmZonesRef,
    FeatureAlarmsRef,
    FeatureCardTypesRef,
    FeatureCardholdersRef,
    FeatureCompetenciesRef,
    FeatureDayCategoriesRef,
    FeatureDivisionsRef,
    FeatureDoorsRef,
    FeatureElevatorsRef,
    FeatureEventsRef,
    FeatureFenceZonesRef,
    FeatureInputsRef,
    FeatureInterlockGroupsRef,
    FeatureItemsRef,
    FeatureLockerBanksRef,
    FeatureMacrosRef,
    FeatureOperatorGroupsRef,
    FeatureOutputsRef,
    FeaturePersonalDataFieldsRef,
    FeatureReceptionsRef,
    FeatureRolesRef,
    FeatureSchedulesRef,
    FeatureVisitsRef,
)


class FeaturesDetail(
    AppBaseModel,
):
    """A detailed list of features that are available on the server.

    All features are marked as Optional, which means that by default
    it's assumed that they are not available on the server. Upon discovery
    if a feature is enabled on the server then we receive a href which
    indicates to the client that the feature is available.

    If a feature is unavailable the API client will throw an exception.
    """

    access_groups: Optional[FeatureAccessGroupsRef] = FeatureAccessGroupsRef()
    access_zones: Optional[FeatureAccessZonesRef] = FeatureAccessZonesRef()
    alarm_zones: Optional[FeatureAlarmZonesRef] = FeatureAlarmZonesRef()
    alarms: Optional[FeatureAlarmsRef] = FeatureAlarmsRef()
    card_types: Optional[FeatureCardTypesRef] = FeatureCardTypesRef()
    cardholders: Optional[FeatureCardholdersRef] = FeatureCardholdersRef()
    competencies: Optional[FeatureCompetenciesRef] = FeatureCompetenciesRef()
    day_categories: Optional[FeatureDayCategoriesRef] = FeatureDayCategoriesRef()
    divisions: Optional[FeatureDivisionsRef] = FeatureDivisionsRef()
    doors: Optional[FeatureDoorsRef] = FeatureDoorsRef()
    elevators: Optional[FeatureElevatorsRef] = FeatureElevatorsRef()
    events: Optional[FeatureEventsRef] = FeatureEventsRef()
    fence_zones: Optional[FeatureFenceZonesRef] = FeatureFenceZonesRef()
    inputs: Optional[FeatureInputsRef] = FeatureInputsRef()
    interlock_groups: Optional[FeatureInterlockGroupsRef] = FeatureInterlockGroupsRef()
    items: Optional[FeatureItemsRef] = FeatureItemsRef()
    locker_banks: Optional[FeatureLockerBanksRef] = FeatureLockerBanksRef()
    macros: Optional[FeatureMacrosRef] = FeatureMacrosRef()
    operator_groups: Optional[FeatureOperatorGroupsRef] = FeatureOperatorGroupsRef()
    outputs: Optional[FeatureOutputsRef] = FeatureOutputsRef()
    personal_data_fields: Optional[FeaturePersonalDataFieldsRef] = (
        FeaturePersonalDataFieldsRef()
    )
    receptions: Optional[FeatureReceptionsRef] = FeatureReceptionsRef()
    roles: Optional[FeatureRolesRef] = FeatureRolesRef()
    schedules: Optional[FeatureSchedulesRef] = FeatureSchedulesRef()
    visits: Optional[FeatureVisitsRef] = FeatureVisitsRef()
