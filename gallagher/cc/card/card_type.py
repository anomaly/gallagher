
from ..utils import APIBase

class CardType(APIBase):

    ENDPOINT = "card_types"

    @classmethod
    def retrieve(cls, id):
        pass

    @classmethod
    def modify(cls):
        pass

    @classmethod
    def create(cls, **params):
        pass
