""" Contains Enumerations for the Gallagher objects

Our naming convention is ObjectIntent

CustomerSearch

"""

from enum import Enum


class SearchSortOrder(str, Enum):
    """Sort descriptors for search operations.
    
    If an endpoint needs to customise the sort order, 
    it should subclass this Enum and add the additional params.
    """

    ID: str = "id"
    ID_DESC: str = "-id"

    NAME: str = "name"
    NAME_DESC: str = "-name"
