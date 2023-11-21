"""


"""

from ..utils import (
    APIEndpoint,
    EndpointConfig
)

from ...dto.day_category import (
    DayCategoryResponse
)


class DayCategory(APIEndpoint):
    """ Day Categories
    """

    __config__ = EndpointConfig(
        endpoint="day_categories",
        dto_list=DayCategoryResponse,
        dto_retrieve=DayCategoryResponse,
    )
