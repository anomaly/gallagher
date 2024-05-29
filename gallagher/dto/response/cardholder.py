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
    def result_set(self) -> list[CardholderSummary]:
        """ Wrap summary response target property

        the sql interface will call this property and each summary
        response is expected to override this and return the appropriate
        target property
        """
        return self.results

    @property
    def cli_header(self):
        return ("id", "first name", "last name", "authorised")

    def __rich_repr__(self):
        return (r.__rich_repr__() for r in self.results)

    def __str__(self):
        return f"{len(self.results)} cardholders"
