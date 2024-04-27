from typing import Optional

from ..utils import (
    AppBaseModel,
    HrefMixin,
)

from ..detail import (
    DivisionDetail
)


class DivisionDetailResponse(
    AppBaseModel
):
    """ Division

    """

    results: list[DivisionDetail]
    next: Optional[HrefMixin] = None

    @property
    def cli_header(self):
        return [
            "Id",
            "Name",
            "Server Display Name",
        ]

    def __rich_repr__(self):
        return [r.__rich_repr__() for r in self.results]

    def __str__(self):
        return f"{len(self.results)} divisions"
