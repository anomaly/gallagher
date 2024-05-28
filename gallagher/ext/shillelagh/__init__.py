""" Adapter and SQLAlchemy dialect for shillelagh

The package provides extensions to provide a SQL interface for the
Gallagher API.

[shillelagh](https://github.com/betodealmeida/shillelagh)
"""
import os
import asyncio
import logging
import urllib

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
from gallagher.cc.alarms import __shillelagh__ \
    as alarms_tables
from gallagher.cc.cardholders import __shillelagh__ \
    as cardholders_tables
from gallagher.cc.status_overrides import __shillelagh__ \
    as status_overrides_tables

# TODO: get rid of this
from gallagher.cc.cardholders import Cardholder
class GallagherCommandCentreAPI(Adapter):

    # Use this to log messages to assist with shillelagh debugging
    _logger = logging.getLogger(__name__)

    # Concatenate all the tables into a single list for efficiency
    # This is declared here because it's accessed by a static method
    # because shillelagh's supports method is static
    _all_tables = alarms_tables + cardholders_tables + \
        status_overrides_tables

    # The adapter doesn't access the filesystem.
    safe = True

    # The adapter will receive a ``limit`` argument in the ``get_data``
    # method, and will be responsible for limiting the number of rows returned.
    supports_limit = True
    supports_offset = True

    # Check to see if we can do this using the partial column feature
    supports_requested_columns = False

    @staticmethod
    def get_endpoint_urls() -> list[str]:
        #TODO: we need to improve performance by cache this
        #NOTE: this is a method because we need bootstrap to run first
        return [
            f"{table.__config__.endpoint.href}" for table \
                in GallagherCommandCentreAPI._all_tables
        ]


    @staticmethod
    def bootstrap_api_client():
        """ Bootstrap the API client for the adapter 
        
        This checks for the availability of the GACC_API_KEY environment
        and sets the variable in the API client
        
        Call this before any operations on the API client
        """
        if not 'GACC_API_KEY' in os.environ:
            raise ValueError(
                "GACC_API_KEY environment variable must be set"
            )

        api_key = os.environ.get('GACC_API_KEY')
        cc.api_key = api_key

        for table in GallagherCommandCentreAPI._all_tables:
            # This should get us the url, and if not then we are in an invalid state
            # Discover should only ever run for the first endpoint and all
            # others should then deffer to the cached property
            # 
            # Running this here saves us from having to run it in other places
            asyncio.run(table._discover())


    @staticmethod
    def supports(uri: str, fast: bool = True, **kwargs: Any) -> Optional[bool]:
        """ Return the URL if it is a Gallagher Command Centre API URL

        GACC requires us to respect the HATEOS principle, so we need to
        run discovery before we can evaluate the URL, this means that we
        require the API key to be present and initialise the client.

        Because we share the cc object across multiple methods, it available
        outside the scope of this method
        """
        GallagherCommandCentreAPI.bootstrap_api_client()
        
        if not uri in GallagherCommandCentreAPI.get_endpoint_urls():
            GallagherCommandCentreAPI._logger.debug(
                f"{uri} not found in {GallagherCommandCentreAPI.get_endpoint_urls()}"
            )
            return False

        # Parse the base url using urlparse for comparison        
        # TODO: ensure this is loaded from the overridden API base
        base_parsed_url = urllib.parse.urlparse(cc.api_base)

        # Parse the endpoint using urlparse
        parsed_url = urllib.parse.urlparse(uri)

        # Match the netloc property to be equal to the api_base
        # and the scheme to be equal to the base_parsed_url
        #
        # Note that do not match the path as it wil be different
        # and it should have passed the check of being in the endpoint_urls
        if not parsed_url.netloc == base_parsed_url.netloc or\
            not parsed_url.scheme == base_parsed_url.scheme:
            return False
        
        return True
        
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

        for table in self._all_tables:
            self._logger.debug(f"Finding suitable adapter for {self.uri}")
            if self.uri == f"{table.__config__.endpoint.href}":
                self._logger.debug(f"Found helper class = {table}")
                return table.__config__.sql_model._shillelagh_columns()
        return {}


    def get_data(  # pylint: disable=too-many-locals
        self,
        bounds: Dict[str, Filter],
        order: List[Tuple[str, RequestedOrder]],
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        **kwargs: Any,
    ) -> Iterator[Row]:
        
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

