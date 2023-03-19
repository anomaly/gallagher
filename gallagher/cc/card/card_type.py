import httpx

from ...schema import CardTypeDetail, Response
from ..utils import get_authorization_headers

class CardType():

    ENDPOINT = "card_types"
    
    @classmethod
    def list(cls, skip=0):
        from .. import api_base
        response = httpx.get(
            f'{api_base}{cls.ENDPOINT}',
            headers=get_authorization_headers(),
        )

        card_holder = Response.parse_obj(response.json())
        return card_holder

    @classmethod
    def retrieve(cls, id):
        pass

    @classmethod
    def modify(cls):
        pass

    @classmethod
    def create(cls, **params):
        pass
