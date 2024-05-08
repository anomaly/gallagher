""" Command Centre API discovery

The Command Centre API has a discovery endpoint that allows

"""

from typing import (
    Optional,
)

from ..utils import (
    AppBaseModel,
    OptionalHrefMixin,
)


class FeatureAccessGroupsRef(
    AppBaseModel,
):
    access_groups: Optional[OptionalHrefMixin] = OptionalHrefMixin()


class FeatureAccessZonesRef(
    AppBaseModel,
):
    access_zones: Optional[OptionalHrefMixin] = OptionalHrefMixin()


class FeatureAlarmZonesRef(
    AppBaseModel,
):
    alarm_zones: Optional[OptionalHrefMixin] = OptionalHrefMixin()


class FeatureAlarmsRef(
    AppBaseModel,
):
    alarms: Optional[OptionalHrefMixin] = OptionalHrefMixin()
    divisions: Optional[OptionalHrefMixin] = OptionalHrefMixin()
    updates: Optional[OptionalHrefMixin] = OptionalHrefMixin()


class FeatureCardTypesRef(
    AppBaseModel,
):
    assign: Optional[OptionalHrefMixin] = OptionalHrefMixin()
    card_types: Optional[OptionalHrefMixin] = OptionalHrefMixin()


class FeatureCardholdersRef(
    AppBaseModel,
):
    cardholders: Optional[OptionalHrefMixin] = OptionalHrefMixin()
    changes: Optional[OptionalHrefMixin] = OptionalHrefMixin()
    update_location_access_zones: Optional[OptionalHrefMixin] = OptionalHrefMixin()


class FeatureCompetenciesRef(
    AppBaseModel,
):
    competencies: Optional[OptionalHrefMixin] = OptionalHrefMixin()


class FeatureDayCategoriesRef(
    AppBaseModel,
):
    day_categories: Optional[OptionalHrefMixin] = OptionalHrefMixin()


class FeatureDivisionsRef(
    AppBaseModel,
):
    divisions: Optional[OptionalHrefMixin] = OptionalHrefMixin()


class FeatureDoorsRef(
    AppBaseModel,
):
    doors: Optional[OptionalHrefMixin] = OptionalHrefMixin()


class FeatureElevatorsRef(
    AppBaseModel,
):
    elevator_groups: Optional[OptionalHrefMixin] = OptionalHrefMixin()


class FeatureEventsRef(
    AppBaseModel,
):
    divisions: Optional[OptionalHrefMixin] = OptionalHrefMixin()
    event_groups: Optional[OptionalHrefMixin] = OptionalHrefMixin()
    events: Optional[OptionalHrefMixin] = OptionalHrefMixin()
    updates: Optional[OptionalHrefMixin] = OptionalHrefMixin()


class FeatureFenceZonesRef(
    AppBaseModel,
):
    fence_zones: Optional[OptionalHrefMixin] = OptionalHrefMixin()


class FeatureInputsRef(
    AppBaseModel,
):
    inputs: Optional[OptionalHrefMixin] = OptionalHrefMixin()


class FeatureInterlockGroupsRef(
    AppBaseModel,
):
    interlock_groups: Optional[OptionalHrefMixin] = OptionalHrefMixin()


class FeatureItemsRef(
    AppBaseModel,
):
    item_types: Optional[OptionalHrefMixin] = OptionalHrefMixin()
    items: Optional[OptionalHrefMixin] = OptionalHrefMixin()
    updates: Optional[OptionalHrefMixin] = OptionalHrefMixin()


class FeatureLockerBanksRef(
    AppBaseModel,
):
    locker_banks: Optional[OptionalHrefMixin] = OptionalHrefMixin()


class FeatureMacrosRef(
    AppBaseModel,
):
    macros: Optional[OptionalHrefMixin] = OptionalHrefMixin()


class FeatureOperatorGroupsRef(
    AppBaseModel,
):
    operator_groups: Optional[OptionalHrefMixin] = OptionalHrefMixin()


class FeatureOutputsRef(
    AppBaseModel,
):
    outputs: Optional[OptionalHrefMixin] = OptionalHrefMixin()


class FeaturePersonalDataFieldsRef(
    AppBaseModel,
):
    personal_data_fields: Optional[OptionalHrefMixin] = OptionalHrefMixin()


class FeatureReceptionsRef(
    AppBaseModel,
):
    receptions: Optional[OptionalHrefMixin] = OptionalHrefMixin()


class FeatureRolesRef(
    AppBaseModel,
):
    roles: Optional[OptionalHrefMixin] = OptionalHrefMixin()


class FeatureSchedulesRef(
    AppBaseModel,
):
    schedules: Optional[OptionalHrefMixin] = OptionalHrefMixin()


class FeatureVisitsRef(
    AppBaseModel,
):
    visits: Optional[OptionalHrefMixin] = OptionalHrefMixin()
