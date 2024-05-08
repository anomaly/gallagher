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
    access_groups: OptionalHrefMixin = OptionalHrefMixin()


class FeatureAccessZonesRef(
    AppBaseModel,
):
    access_zones: OptionalHrefMixin = OptionalHrefMixin()


class FeatureAlarmZonesRef(
    AppBaseModel,
):
    alarm_zones: OptionalHrefMixin = OptionalHrefMixin()


class FeatureAlarmsRef(
    AppBaseModel,
):
    alarms: OptionalHrefMixin = OptionalHrefMixin()
    divisions: OptionalHrefMixin = OptionalHrefMixin()
    updates: OptionalHrefMixin = OptionalHrefMixin()


class FeatureCardTypesRef(
    AppBaseModel,
):
    assign: OptionalHrefMixin = OptionalHrefMixin()
    card_types: OptionalHrefMixin = OptionalHrefMixin()


class FeatureCardholdersRef(
    AppBaseModel,
):
    cardholders: OptionalHrefMixin = OptionalHrefMixin()
    changes: OptionalHrefMixin = OptionalHrefMixin()
    update_location_access_zones: OptionalHrefMixin = OptionalHrefMixin()


class FeatureCompetenciesRef(
    AppBaseModel,
):
    competencies: OptionalHrefMixin = OptionalHrefMixin()


class FeatureDayCategoriesRef(
    AppBaseModel,
):
    day_categories: OptionalHrefMixin = OptionalHrefMixin()


class FeatureDivisionsRef(
    AppBaseModel,
):
    divisions: OptionalHrefMixin = OptionalHrefMixin()


class FeatureDoorsRef(
    AppBaseModel,
):
    doors: OptionalHrefMixin = OptionalHrefMixin()


class FeatureElevatorsRef(
    AppBaseModel,
):
    elevator_groups: OptionalHrefMixin = OptionalHrefMixin()


class FeatureEventsRef(
    AppBaseModel,
):
    divisions: OptionalHrefMixin = OptionalHrefMixin()
    event_groups: OptionalHrefMixin = OptionalHrefMixin()
    events: OptionalHrefMixin = OptionalHrefMixin()
    updates: OptionalHrefMixin = OptionalHrefMixin()


class FeatureFenceZonesRef(
    AppBaseModel,
):
    fence_zones: OptionalHrefMixin = OptionalHrefMixin()


class FeatureInputsRef(
    AppBaseModel,
):
    inputs: OptionalHrefMixin = OptionalHrefMixin()


class FeatureInterlockGroupsRef(
    AppBaseModel,
):
    interlock_groups: OptionalHrefMixin = OptionalHrefMixin()


class FeatureItemsRef(
    AppBaseModel,
):
    item_types: OptionalHrefMixin = OptionalHrefMixin()
    items: OptionalHrefMixin = OptionalHrefMixin()
    updates: OptionalHrefMixin = OptionalHrefMixin()


class FeatureLockerBanksRef(
    AppBaseModel,
):
    locker_banks: OptionalHrefMixin = OptionalHrefMixin()


class FeatureMacrosRef(
    AppBaseModel,
):
    macros: OptionalHrefMixin = OptionalHrefMixin()


class FeatureOperatorGroupsRef(
    AppBaseModel,
):
    operator_groups: OptionalHrefMixin = OptionalHrefMixin()


class FeatureOutputsRef(
    AppBaseModel,
):
    outputs: OptionalHrefMixin = OptionalHrefMixin()


class FeaturePersonalDataFieldsRef(
    AppBaseModel,
):
    personal_data_fields: OptionalHrefMixin = OptionalHrefMixin()


class FeatureReceptionsRef(
    AppBaseModel,
):
    receptions: OptionalHrefMixin = OptionalHrefMixin()


class FeatureRolesRef(
    AppBaseModel,
):
    roles: OptionalHrefMixin = OptionalHrefMixin()


class FeatureSchedulesRef(
    AppBaseModel,
):
    schedules: OptionalHrefMixin = OptionalHrefMixin()


class FeatureVisitsRef(
    AppBaseModel,
):
    visits: OptionalHrefMixin = OptionalHrefMixin()
