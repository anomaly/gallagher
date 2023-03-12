
from gallagher import cc

def check_api_key_format():
    """
    
    """
    return False

def get_authorization_headers():
    print(cc.api_key)
    return {
        "Authorization": "GGL-API-KEY"
    }
