""" Command Centre API discovery

The Command Centre API has a discovery endpoint that allows

"""

from ..utils import (
    AppBaseModel,
    OptionalHrefMixin,
)


class FeatureAccessGroupsRef(
    AppBaseModel,
):
    access_groups: OptionalHrefMixin = None


class FeatureAccessZonesRef(
    AppBaseModel,
):
    access_zones: OptionalHrefMixin = None


class FeatureAlarmZonesRef(
    AppBaseModel,
):
    alarm_zones: OptionalHrefMixin = None


class FeatureAlarmsRef(
    AppBaseModel,
):
    alarms: OptionalHrefMixin = None
    divisions: OptionalHrefMixin = None
    updates: OptionalHrefMixin = None


class FeatureCardTypesRef(
    AppBaseModel,
):
    assign: OptionalHrefMixin = None
    card_types: OptionalHrefMixin = None


class FeatureCardholdersRef(
    AppBaseModel,
):
    cardholders: OptionalHrefMixin = None
    changes: OptionalHrefMixin = None
    update_location_access_zones: OptionalHrefMixin = None


class FeatureCompetenciesRef(
    AppBaseModel,
):
    competencies: OptionalHrefMixin = None


class FeatureDayCategoriesRef(
    AppBaseModel,
):
    day_categories: OptionalHrefMixin = None


class FeatureDivisionsRef(
    AppBaseModel,
):
    divisions: OptionalHrefMixin = None


class FeatureDoorsRef(
    AppBaseModel,
):
    doors: OptionalHrefMixin = None


class FeatureElevatorsRef(
    AppBaseModel,
):
    elevator_groups: OptionalHrefMixin = None


class FeatureEventsRef(
    AppBaseModel,
):
    divisions: OptionalHrefMixin = None
    event_groups: OptionalHrefMixin = None
    events: OptionalHrefMixin = None
    updates: OptionalHrefMixin = None


class FeatureFenceZonesRef(
    AppBaseModel,
):
    fence_zones: OptionalHrefMixin = None


class FeatureInputsRef(
    AppBaseModel,
):
    inputs: OptionalHrefMixin = None


class FeatureInterlockGroupsRef(
    AppBaseModel,
):
    interlock_groups: OptionalHrefMixin = None


class FeatureItemsRef(
    AppBaseModel,
):
    item_types: OptionalHrefMixin = None
    items: OptionalHrefMixin = None
    updates: OptionalHrefMixin = None


class FeatureLockerBanksRef(
    AppBaseModel,
):
    locker_banks: OptionalHrefMixin = None


class FeatureMacrosRef(
    AppBaseModel,
):
    macros: OptionalHrefMixin = None


class FeatureOperatorGroupsRef(
    AppBaseModel,
):
    operator_groups: OptionalHrefMixin = None


class FeatureOutputsRef(
    AppBaseModel,
):
    outputs: OptionalHrefMixin = None


class FeaturePersonalDataFieldsRef(
    AppBaseModel,
):
    personal_data_fields: OptionalHrefMixin = None


class FeatureReceptionsRef(
    AppBaseModel,
):
    receptions: OptionalHrefMixin = None


class FeatureRolesRef(
    AppBaseModel,
):
    roles: OptionalHrefMixin = None


class FeatureSchedulesRef(
    AppBaseModel,
):
    schedules: OptionalHrefMixin = None


class FeatureVisitsRef(
    AppBaseModel,
):
    visits: OptionalHrefMixin = None
