""" Personal Data Fields

"""
from ..utils import (
    AppBaseModel,
)

from ..ref import (
    PDFRef,
)


class PdfResponse(
    AppBaseModel,
):
    results: list[PDFRef]
