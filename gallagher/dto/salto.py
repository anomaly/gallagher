"""


"""

from .utils import (
    AppBaseModel,
    HrefMixin
)

from .schedule import ScheduleRef

class SaltoItemTypeRef(
    AppBaseModel,
):
    """ A Salto Item Type is a SALTO product category e.g door
    """
    value: str

class SaltoItemRef(
    AppBaseModel,
    HrefMixin
):
    """ A Salto Item is a particular product e.g Salto CU5000
    """
    name: str

class SaltoAccessItemSummary(
    AppBaseModel,
):
    """ A Summary of Salto items

    """
    salto_item_type: SaltoItemTypeRef
    salto_item: SaltoItemRef
    schedule: ScheduleRef