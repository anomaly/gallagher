""" Utilities for the Gallagher Command Centre API

"""
import httpx

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
    """ Base class for all API objects

    All API endpoints must inherit from this class and provide a Config class
    that automates the implementation of many of the API methods.

    If the endpoints provide additional methods then they are to implement them
    based on the same standards as this base class.

    """

    class Config:
        """
        
        """
        endpoint = None
        list_response_class = None
        retrieve_response_class = None

        top = 10
        sort = "id" # Can be set to id or -id
        fields = []

    @classmethod
    def _discover(cls):
        pass

    @classmethod
    def list(cls, skip=0):
        """ For a list of objects for the given resource

        Most resources can be searched which is exposed by this method.
        Resources also allow pagination which can be controlled by the skip
        """
        from . import api_base
        response = httpx.get(
            f'{api_base}{cls.Config.endpoint}',
            headers=get_authorization_headers(),
        )

        parsed_obj = cls.Config.list_response_class.model_validate(
            response.json()
        )

        return parsed_obj

    @classmethod
    def retrieve(cls, id):
        """ Retrieve a single object for the given resource

        Most objects have an ID which is numeral or UUID. 
        Each resource also provides a href and pagination for
        children.
        """
        from . import api_base
        response = httpx.get(
            f'{api_base}{cls.Config.endpoint}/{id}',
            headers=get_authorization_headers(),
        )

        parsed_obj = cls.Config.retrieve_response_class.model_validate(
            response.json()
        )

        return parsed_obj

    @classmethod
    def modify(cls):
        """
        
        """
        pass

    @classmethod
    def create(cls, **params):
        """
        
        """
        pass

    @classmethod
    def delete(cls):
        """
        
        """
        pass

    @classmethod
    def search(cls):
        """
        
        """
        pass
