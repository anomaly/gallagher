""" Adapter and SQLAlchemy dialect for shillelagh

The package provides extensions to provide a SQL interface for the
Gallagher API.

[shillelagh](https://github.com/betodealmeida/shillelagh)
"""
import urllib
import os

# import logging
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

# logging.error("test")

from typing import (
    Any,
    Dict,
    Iterator,
    AsyncIterator,
    List, 
    Optional,
    Tuple,
)

from shillelagh.adapters.base import Adapter
from shillelagh.typing import (
    RequestedOrder, 
    Row,
)
from shillelagh.filters import (
    Filter,
    Impossible,
    Operator,
    Range,
)

from shillelagh.fields import (
    Float,
    Integer,
    String,
    Order,
    Boolean,
)

# TODO: refactor this to generic based on SQL.md
from gallagher import cc
from gallagher.cc.cardholders.cardholders import Cardholder


class GallagherCommandCentreAPI(Adapter):

    # The adapter doesn't access the filesystem.
    safe = True

    # The adapter will receive a ``limit`` argument in the ``get_data``
    # method, and will be responsible for limiting the number of rows returned.
    supports_limit = True
    supports_offset = True

    # Check to see if we can do this using the partial column feature
    supports_requested_columns = False

    # Columns
    first_name = String()
    last_name = String()
    id = Integer()
    authorised = Boolean()


    @staticmethod
    def supports(uri: str, fast: bool = True, **kwargs: Any) -> Optional[bool]:
        # return true if the url is acceptable to us
        parsed = urllib.parse.urlparse(uri)
        query_string = urllib.parse.parse_qs(parsed.query)
        return (
            parsed.netloc == "commandcentre-api-au.security.gallagher.cloud"
        )

    @staticmethod
    def parse_uri(uri: str) -> Tuple[str]:
        return (uri, os.environ.get('GACC_API_KEY'))

    def __init__(self, uri: str, api_key: Optional[str], **kwargs: Any):
        super().__init__()

        self.uri = uri
        cc.api_key = api_key

    def get_data(  # pylint: disable=too-many-locals
        self,
        bounds: Dict[str, Filter],
        order: List[Tuple[str, RequestedOrder]],
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        **kwargs: Any,
    ) -> Iterator[Row]:
        
        # TODO: refactor this to see if can support asyncio
        import asyncio
        cardholders = asyncio.run(Cardholder.list())
        # cardholders = await Cardholder.list()

        rindex = 0

        for row in cardholders.results:

            yield {
                "rowid": row.id,
                "id": row.id,
                "authorised": row.authorised,
                "first_name": row.first_name,
                "last_name": row.last_name,
            }

            rindex += 1
            if rindex == limit:
                break

