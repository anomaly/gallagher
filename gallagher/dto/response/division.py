from typing import Optional

from ..utils import (
    HrefMixin,
    AppBaseResponseWithFollowModel,
)

from ..summary import DivisionSummary

from ..detail import DivisionDetail


class DivisionSummaryResponse(
    AppBaseResponseWithFollowModel,
):
    """Division Summary

    This should return the summary and as per the documentation
    the detail should have more than what we have here

    TODO: check this is different

    """

    results: list[DivisionSummary]

    @property
    def cli_header(self):
        return (
            "id",
            "name",
            "server display name",
        )

    def __rich_repr__(self):
        return (r.__rich_repr__() for r in self.results)

    def __str__(self):
        return f"{len(self.results)} divisions"
