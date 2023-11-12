""" Personal Data Fields (not to be confused with PDF files)

"""

from typing import Optional

from .utils import AppBaseModel, IdentityMixin,\
    HrefMixin

class PDFRef(
    AppBaseModel,
    HrefMixin
):
    """ Personal Data Fields are custom fields for a card holder
    """
    name: str

class PDFDetail(
    PDFRef
):
    """ Personal Data Fields are custom fields for a card holder
    """
    description: Optional[str]
    division: IdentityMixin
    server_display_name: Optional[str]
