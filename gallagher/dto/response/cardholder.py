"""

"""

from ..utils import (
    AppBaseResponseModel,
)

from ..summary import CardholderSummary


class CardholderSummaryResponse(
    AppBaseResponseModel,
):
    """Summary response for cardholder list and search

    /api/cardholders is generally the endpoint that responds
    to the query, it is dynamically configured from the discovery

    """

    results: list[CardholderSummary]

    @property
    def cli_header(self):
        return ["Id", "First name", "Last name", "Authorised"]

    def __rich_repr__(self):
        return [r.__rich_repr__() for r in self.results]

    def __str__(self):
        return f"{len(self.results)} cardholders"
