
from ..utils import APIBase
from ...schema.card_type import CardTypeResponse

class CardType(APIBase):
    """
    
    """

    class Config:

        endpoint = "card_types"
        response_class = CardTypeResponse

