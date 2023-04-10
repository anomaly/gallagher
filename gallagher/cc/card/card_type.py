
from ..utils import APIBase
from ...schema.card_type import CardTypeResponse

class CardType(APIBase):

    ENDPOINT = "card_types"
    RESPONSE_CLASS = CardTypeResponse

    @classmethod
    def retrieve(cls, id):
        pass

    @classmethod
    def modify(cls):
        pass

    @classmethod
    def create(cls, **params):
        pass
