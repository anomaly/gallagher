""" Adapter and SQLAlchemy dialect for shillelagh

The package provides extensions to provide a SQL interface for the
Gallagher API.

[shillelagh](https://github.com/betodealmeida/shillelagh)
"""
import urllib


import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

logging.error("test")

from typing import (
    Any,
    Dict,
    Iterator,
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

class GallagherCommandCentreAPI(Adapter):

    # The adapter doesn't access the filesystem.
    safe = True

    # The adapter will receive a ``limit`` argument in the ``get_data``
    # method, and will be responsible for limiting the number of rows returned.
    supports_limit = True

    supports_offset = False

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
        return (uri, "api_key")

    def __init__(self, uri: str, api_key: Optional[str], **kwargs: Any):
        super().__init__()

        self.uri = uri
        self.api_key = api_key

    def get_data(  # pylint: disable=too-many-locals
        self,
        bounds: Dict[str, Filter],
        order: List[Tuple[str, RequestedOrder]],
        **kwargs: Any,
    ) -> Iterator[Dict[str, Any]]:
        yield {
            "rowid": 1,
            "id": 1,
            "authorised": True,
            "first_name": "Dev",
            "last_name": "Mukherjee",
        }
