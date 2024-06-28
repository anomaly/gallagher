""" Enumerations

This module contains enumerations used in the DTOs. Enums can be shared
across ref, detail, response, and summary DTOs.

Each one of these aligns with the API documentation and is used to
ensure that we are receive or send the correct values.
"""
from enum import Enum

class PdfType(str, Enum):
    """ Personal Data Field Types

    Types of acceptable personal data fields allowed by the server
    these are in accordance with the API endpoints
    """
    STRING = "string"
    IMAGE = "image"
    STR_ENUM = "strEnum"
    NUMERIC = "numeric"
    DATE = "date"
    ADDRESS = "address"
    PHONE = "phone"
    EMAIL = "email"
    MOBILE = "mobile"


class CredentialsClass(str, Enum):
    """ Credential Class related to different card types

    A card type must be one of the following credential classes
    """
    CARD = "card"
    DIGITAL_ID = "digitalId"
    GOV_PASS = "govPass"
    MOBILE = "mobile"
    PVI = "piv"
    PIVI = "pivi"
    TRACKING_TAG = "trackingTag"
    TRANSACT = "transact"
    FIOD2 = "fido2"