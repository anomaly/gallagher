"""

"""
import httpx

from ..schema import Response

def check_api_key_format(api_key):
    """
    
    """
    api_tokens = api_key.split('-')
    return (api_tokens.count() == 8)

def get_authorization_headers():
    """
    
    """
    from . import api_key
    return {
        'Authorization': f'GGL-API-KEY {api_key}'
    }

class APIBase():
    """
    
    """

    ENDPOINT = None
    RESPONSE_CLASS = None

    TOP = 10
    SORT = "id" # Can be set to id or -id
    FIELDS = []

    @classmethod
    def list(cls, skip=0):
        from . import api_base
        response = httpx.get(
            f'{api_base}{cls.ENDPOINT}',
            headers=get_authorization_headers(),
        )

        card_holder = Response.parse_obj(response.json())
        return card_holder
