"""


"""

from ..core import Capabilities, APIEndpoint, EndpointConfig

from ...dto.response import DayCategoryResponse


class DayCategory(APIEndpoint):
    """Day Categories"""

    def get_config(self) -> EndpointConfig:
        return EndpointConfig(
            endpoint=Capabilities.CURRENT.features.day_categories.day_categories,
            dto_list=DayCategoryResponse,
            dto_retrieve=DayCategoryResponse,
        )
