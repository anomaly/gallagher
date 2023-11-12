"""


"""

from ..utils import (
    APIBase,
    EndpointConfig
)

from ...dto.day_category import (
    DayCategoryResponse
)


class DayCategory(APIBase):
    """ Day Categories
    """

    __config__ = EndpointConfig(
        endpoint="day_categories",
        dto_list=DayCategoryResponse,
        dto_retrieve=DayCategoryResponse,
    )
