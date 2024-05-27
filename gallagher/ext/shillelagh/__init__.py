""" Adapter and SQLAlchemy dialect for shillelagh

The package provides extensions to provide a SQL interface for the
Gallagher API.

[shillelagh](https://github.com/betodealmeida/shillelagh)
"""
import os

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')
# logging.basicConfig(level=logging.ERROR, format='%(asctime)s %(levelname)s %(message)s')

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
    Field,
    Float,
    Integer,
    String,
    Order,
    Boolean,
)

# TODO: refactor this to generic based on SQL.md
from gallagher import cc
from gallagher.cc.vtables import VirtualTableHelper
from gallagher.cc.cardholders import Cardholder

# TODO: see if this can be made more efficient
if not 'GACC_API_KEY' in os.environ:
    raise ValueError(
        "GACC_API_KEY environment variable must be set"
    )

# TODO: see if this can be made more efficient
api_key = os.environ.get('GACC_API_KEY')
cc.api_key = api_key

# This is initialised after the API key is set
_adapter_helper = VirtualTableHelper()

class GallagherCommandCentreAPI(Adapter):

    # The adapter doesn't access the filesystem.
    safe = True

    # The adapter will receive a ``limit`` argument in the ``get_data``
    # method, and will be responsible for limiting the number of rows returned.
    supports_limit = True
    supports_offset = True

    # Check to see if we can do this using the partial column feature
    supports_requested_columns = False

    @staticmethod
    def supports(uri: str, fast: bool = True, **kwargs: Any) -> Optional[bool]:
        """ Return the URL if it is a Gallagher Command Centre API URL

        GACC requires us to respect the HATEOS principle, so we need to
        run discovery before we can evaluate the URL, this means that we
        require the API key to be present and initialise the client.

        Because we share the cc object across multiple methods, it available
        outside the scope of this method
        """
        
        # Process the URL to see if it's valid based on
        # the configuration of the development environment
        return _adapter_helper.is_valid_endpoint(uri)

    @staticmethod
    def parse_uri(uri: str) -> Tuple[str, str]:
        """ 

        Returns:
            Tuple[str, str]: The URI and the API key
        """
        return (uri, os.environ.get('GACC_API_KEY'))

    def __init__(self, uri: str, api_key: Optional[str], **kwargs: Any):

        super().__init__()

        self.uri = uri
        # TODO: might be redundant due to moving this up the package level
        cc.api_key = api_key


    def get_columns(self) -> Dict[str, Field]:

        cols = _adapter_helper.get_columns(self.uri)
        import logging
        print(cols)
        return cols

        # Columns
        # return {
        #     # "id": Integer(),
        #     "authorised": Boolean(),
        #     "first_name": String(),
        #     "last_name": String(),
        #     "short_name": String(),
        #     "description": String(),
        # }


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

