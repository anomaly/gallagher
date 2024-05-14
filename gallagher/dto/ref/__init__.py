""" Reference classes

Our design outlines three types of DTO classes, Refs are ones that are
used to reference other objects, think of them as interlinks between
objects. They usually contain a href and some identifying information
such as a name or id.

This package was introduced in reference to this issue 
https://github.com/anomaly/gallagher/issues/21

which identified race conditions with circular imports. This is caused
mostly because of the nature of the data that the command centre exposes.
"""

from .access_group import AccessGroupRef

from .alarm import (
    AlarmRef,
    AlarmZoneRef,
)

from .card_type import (
    CardTypeRef,
)

from .cardholder import (
    CardholderRef,
    CardholderExtendedRef,
)

from .day_category import (
    DayCategoryRef,
)

from .discover import (
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

from .division import (
    DivisionRef,
)

from .door import (
    DoorRef,
)

from .event import (
    EventGroupRef,
)

from .ext import (
    PlaceholderRef,
)

from .items import (
    ItemRef,
)

from .pdf import (
    PDFRef,
)

from .salto import (
    SaltoItemTypeRef,
    SaltoItemRef,
)

from .schedule import (
    ScheduleRef,
)


from .misc import (
    InstructionRef,
)

from .operator import (
    OperatorRef,
)

from .role import (
    RoleRef,
)

from .zone import (
    AccessZoneRef,
)
