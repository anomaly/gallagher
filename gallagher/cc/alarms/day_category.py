"""


"""

from ..core import (
    Capabilities,
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
            endpoint=Capabilities.CURRENT.features.day_categories
            .day_categories.href,
            dto_list=DayCategoryResponse,
            dto_retrieve=DayCategoryResponse,
        )
