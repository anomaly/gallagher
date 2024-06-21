""" Personal Data Field Summary
"""
from ..enum import PdfType

from ..utils import (
    AppBaseModel,
    HrefMixin,
    IdentityMixin,
)

class PdfSummary(
    AppBaseModel,
    HrefMixin,
    IdentityMixin,
):
    """ Personal Data Field Summary

    Primarily used as the definition in the Cardholder response
    """
    
    name: str
    type: PdfType # See gallagher docs for enum