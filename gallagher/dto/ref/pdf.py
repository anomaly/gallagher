""" Personal Data Fields

Custom fields defined per command centre installation, these need
to be discovered ahead of time before we work with them.

Note:
- Keys are prefixed with @
- Presence of space in the field name
"""

from ..utils import (
    AppBaseModel,
    IdentityMixin,
    HrefMixin,
)


class PDFRef(AppBaseModel, IdentityMixin, HrefMixin):
    """Personal Data Fields are custom fields for a card holder

    These are defined per command centre installation and the fields
    are prefixed with @ e.g @Personal URL, note the presence of the space
    in the field name.

    Since they are dynamic we will have to discover the personal data
    fields much like the URL discovery before we are able to parse the data
    """

    name: str
