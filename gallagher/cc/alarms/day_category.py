"""


"""

from ..core import APIEndpoint, EndpointConfig

from ...dto.response import DayCategoryResponse


class DayCategory(APIEndpoint):
    """Day Categories"""

    def get_config(self) -> EndpointConfig:
        return EndpointConfig(
            endpoint=self._CAPABILITIES.features.day_categories.day_categories,
            dto_list=DayCategoryResponse,
            dto_retrieve=DayCategoryResponse,
        )
