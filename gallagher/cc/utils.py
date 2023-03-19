"""

"""

def check_api_key_format():
    """
    
    """
    return False

def get_authorization_headers():
    from . import api_key
    return {
        "Authorization": f'GGL-API-KEY {api_key}'
    }
