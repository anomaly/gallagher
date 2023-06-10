"""


"""

from ..utils import APIBase
from ...schema.day_category import DayCategoryResponse


class DayCategory(APIBase):
    """ Day Categories
    """

    class Config:
        
        endpoint = "day_categories"
        list_response_class = DayCategoryResponse
