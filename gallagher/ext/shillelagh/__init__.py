""" Adapter and SQLAlchemy dialect for shillelagh

The package provides extensions to provide a SQL interface for the
Gallagher API.

[shillelagh](https://github.com/betodealmeida/shillelagh)
"""
import os
import asyncio
import logging
import urllib
from datetime import datetime

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

from shillelagh.exceptions import (
    ImpossibleFilterError,
    InterfaceError,
    InternalError,
    ProgrammingError,
    UnauthenticatedError,
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
    DateTime,
    Collection,
    Blob,
)

# TODO: refactor this to generic based on SQL.md
from gallagher import cc
from gallagher.cc.alarms import __shillelagh__ \
    as alarms_tables
from gallagher.cc.cardholders import __shillelagh__ \
    as cardholders_tables
from gallagher.cc.status_overrides import __shillelagh__ \
    as status_overrides_tables

class CCAPIAdapter(Adapter):

    # Use this to log messages to assist with shillelagh debugging
    _logger = logging.getLogger(__name__)

    # Concatenate all the tables into a single list for efficiency
    # This is declared here because it's accessed by a static method
    # because shillelagh's supports method is static
    _all_tables = alarms_tables + cardholders_tables + \
        status_overrides_tables

    # Maps the python types to the shillelagh fields
    # initialised here so we don't have to keep redefining it
    _type_map = {
        int: Integer,
        str: String,
        bool: Boolean,
        bytes: Blob,
        list: Collection,
        datetime: DateTime,
        float: Float,
    }

    # API endpoint being used to parse this URL
    # TODO: see if this changes with every instantiation
    _api_endpoint = None

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
        # TODO: we need to improve performance by cache this
        # NOTE: this is a method because we need bootstrap to run first
        return [
            f"{table.__config__.endpoint.href}" for table \
                in CCAPIAdapter._all_tables
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

        if not api_key:
            raise UnauthenticatedError(
                "GACC_API_KEY environment variable must be set"
            )
        
        cc.api_key = api_key

        for table in CCAPIAdapter._all_tables:
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
        CCAPIAdapter.bootstrap_api_client()

        if not uri in CCAPIAdapter.get_endpoint_urls():
            CCAPIAdapter._logger.debug(
                f"{uri} not found in {CCAPIAdapter.get_endpoint_urls()}"
            )
            return False

        # Parse the base url using urlparse for comparison        
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

        self._logger.debug(f"Finding suitable adapter for {self.uri}")

        self._api_endpoint = next(
            (table for table in self._all_tables if self.uri == f"{table.__config__.endpoint.href}"),
            None
        )

        if self._api_endpoint:
            self._logger.debug(f"Found helper class = {self._api_endpoint}")
        else:
            self._logger.debug("No suitable adapter found.")

    def get_columns(self) -> Dict[str, Field]:
        """Return a pyndatic DTO as shil compatible attribute config

        Rules here are that we translate as many dictionary vars into
        a __shillelagh__ compatible format.

        If they are hrefs to other children then we select the id field for
        each one of those objects
        """

        if not self._api_endpoint:
            self._logger.debug("No suitable adapter found while get_columns.")
            return {}

        return {
            key: self._type_map[value]() # shillelagh requires an instance
            for key, value in \
                self._api_endpoint.__config__.dto_retrieve._accumulated_annotations()
            if not key.startswith("_") and value in self._type_map
        }


    def get_data(  # pylint: disable=too-many-locals
        self,
        bounds: Dict[str, Filter],
        order: List[Tuple[str, RequestedOrder]],
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        **kwargs: Any,
    ) -> Iterator[Row]:
        
        dto_list = asyncio.run(self._api_endpoint.list())

        for row in dto_list.result_set:

            yield {
                'rowid': row.id, # Append this for shillelagh
                **row.dict(), # Rest of the responses 
            }

