from ..utils import (
    AppBaseModel,
)

from ..ref import (
    ScheduleRef,
    SaltoItemRef,
    SaltoItemTypeRef,
)


class SaltoAccessItemSummary(
    AppBaseModel,
):
    """A Summary of Salto items"""

    salto_item_type: SaltoItemTypeRef
    salto_item: SaltoItemRef
    schedule: ScheduleRef
