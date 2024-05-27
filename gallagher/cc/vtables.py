""" Virtual Table for Shillelagh

This package is intend

Methods are still called synchronously, this should be refactored 
when shillelagh supports async methods.

"""
import asyncio
import urllib
import logging

from functools import cached_property

from .alarms import __shillelagh__ as alarms_tables
from .cardholders import __shillelagh__ as cardholders_tables
from .status_overrides import __shillelagh__ as status_overrides_tables

from ..cc import api_base

# Iterate _all_tables and get the endpoint url
class VirtualTableHelper():
    """ Virutal Table Helper for Shillelagh

    Note that this should be initialised after the api key has been set
    and the environment has registered the shillelagh adapter. 

    We should always test this via the shillelagh console and then via
    SQLAlchemy.
    """

    _logger = logging.getLogger(__name__)

    def __init__(self):

        self._all_tables = alarms_tables + cardholders_tables + \
            status_overrides_tables

        for table in self._all_tables:
            # This should get us the url, and if not then we are in an invalid state
            # Discover should only ever run for the first endpoint and all
            # others should then deffer to the cached property
            # 
            # Running this here saves us from having to run it in other places
            self._logger.debug(f"Discovering endpoint for {table}")
            asyncio.run(table._discover())

    @cached_property
    def endpoint_urls(self):
        """ All endpoints for registered virtual tables"""
        return [
            f"{table.__config__.endpoint.href}" for table in self._all_tables
        ]

    def is_valid_endpoint(self, uri: str) -> bool:
        """ Check if the uri is a valid endpoint """
        if not uri in self.endpoint_urls:
            self._logger.debug(f"{uri} not found in {self.endpoint_urls}")            
            return False

        # Parse the base url using urlparse for comparison        
        base_parsed_url = urllib.parse.urlparse(api_base)

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

    def get_columns(self, uri: str):
        """ Get the columns for the uri """
        for table in self._all_tables:
            self._logger.debug(f"Finding suitable adapter for {uri}")
            if uri == f"{table.__config__.endpoint.href}":
                self._logger.debug(f"Found helper class = {table}")
                return table.__config__.sql_model.__shillelagh__()
        return {}


