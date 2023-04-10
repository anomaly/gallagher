
from ..utils import APIBase
from ...schema.card_type import CardTypeResponse

class CardType(APIBase):

    ENDPOINT = "card_types"
    RESPONSE_CLASS = CardTypeResponse

