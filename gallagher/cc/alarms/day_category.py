"""


"""

from ..core import (
    APIEndpoint,
    EndpointConfig
)

from ...dto.day_category import (
    DayCategoryResponse
)


class DayCategory(APIEndpoint):
    """ Day Categories
    """

    @classmethod
    def get_config(cls):
        return EndpointConfig(
            endpoint=APIEndpoint._capabilities.features.day_categories
            .day_categories.href,
            dto_list=DayCategoryResponse,
            dto_retrieve=DayCategoryResponse,
        )
