""" Enumerations

This module contains enumerations used in the DTOs. Enums can be shared
across ref, detail, response, and summary DTOs.

Each one of these aligns with the API documentation and is used to
ensure that we are receive or send the correct values.
"""
from enum import Enum

# Pdf type enumeration
# string, image, strEnum, numeric, date, address, phone, email, mobile

class PdfType(str, Enum):
    string = "string"
    image = "image"
    strEnum = "strEnum"
    numeric = "numeric"
    date = "date"
    address = "address"
    phone = "phone"
    email = "email"
    mobile = "mobile"


class CredentialsClass(str, Enum):    
    card = "card"
    digitalId = "digitalId"
    govPass = "govPass"
    mobile = "mobile"
    piv = "piv"
    pivi = "pivi"
    trackingTag = "trackingTag"
    transact = "transact"