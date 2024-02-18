""" Contains Enumerations for the Gallagher objects

Our naming convention is ObjectIntent

CustomerSearch

"""
from enum import Enum


class CustomerSort(Enum):
    """ Sort descriptors for the Customer object

    """

    ID: str = "id"
    ID_DESC: str = "-id"

    NAME: str = "name"
    NAME_DESC: str = "-name"
