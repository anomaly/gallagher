""" 


"""

def setup_module(module):
    """ The Gallagher API client requires a test key, this is 
    set in the environment variable GACC_API_KEY.

    For obvious security reasons never store or version a key
    in the source.
    """
    import os
    api_key = os.environ.get("GACC_API_KEY")
    
    from gallagher import cc
    cc.api_key = api_key


def teardown_module(module):
    """ When we are done running the tests return the API client
    to it's default state.

    This ensures that anything that runs past this point is not
    accessing the server
    """
    from gallagher import cc
    cc.api_key = None
