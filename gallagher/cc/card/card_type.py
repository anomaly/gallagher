
from ..utils import APIBase
from ...schema.card_type import CardTypeResponse

class CardType(APIBase):
    """ Card Types provide a list of support card types for the instance.

    These can vary between using physical cards, mobile credentials, or
    biometrics. The card type is used to dynamically determine the types 
    of credentials available on this particular instance.  
    """

    class Config:

        endpoint = "card_types"
        list_response_class = CardTypeResponse

