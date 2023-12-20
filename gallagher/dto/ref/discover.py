""" Command Centre API discovery

The Command Centre API has a discovery endpoint that allows

"""

from typing import (
    Optional,
)

from ..utils import (
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
