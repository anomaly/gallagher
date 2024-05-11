""" Personal Data Fields

Dynamically occurring fields are defined per site and are
prefixed by an @ symbol as the key of the field, as they
appear in the API responses.

These fields appear either under the personalDataFields as
href references or as individual fields in the user's profile.

"""

from ..utils import (
    AppBaseResponseModel,
)

from ..ref import (
    PDFRef,
)


class PdfResponse(
    AppBaseResponseModel,
):
    """Personal Definition fields

    Returned as a set of results, each result is a PDFRef
    these are to be cached just as we do the URL endpoints,
    note that this must be done after the discovery completes
    """

    results: list[PDFRef]
