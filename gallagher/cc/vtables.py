""" Virtual Table for Shillelagh

This package is intend

Methods are still called synchronously, this should be refactored 
when shillelagh supports async methods.

"""
import asyncio
import urllib

from functools import cached_property

from .alarms import __shillelagh__ as alarms_tables
from .cardholders import __shillelagh__ as cardholders_tables
from .status_overrides import __shillelagh__ as status_overrides_tables

from ..cc import api_base

# Iterate _all_tables and get the endpoint url
class VirtualTableHelper():

    def __init__(self):

        self._all_tables = alarms_tables + cardholders_tables + \
            status_overrides_tables

        for table in self._all_tables:
            # This should get us the url, and if not then we are in an invalid state
            # Discover should only ever run for the first endpoint and all
            # others should then deffer to the cached property
            # 
            # Running this here saves us from having to run it in other places
            import logging
            logging.error(table)

            asyncio.run(table._discover())

    @cached_property
    def endpoint_urls(self):
        """ All endpoints for registered virtual tables"""
        for table in self._all_tables:
            __config__ = asyncio.run(table.get_config())
            print(__config__.endpoint)

        return []

    def is_valid_endpoint(self, uri: str) -> bool:
        """ Check if the uri is a valid endpoint """
        import logging
        logging.error(self.endpoint_urls)

        if not uri in self.endpoint_urls:
            return False
        
        # Parse the endpoint using urlparse
        parsed_url = urllib.parse.urlparse(uri)

        import logging
        logging.error(parsed_url.netloc)

        # Match the netloc property to be equal to the api_base
        if parsed_url.netloc != api_base:
            return False
        
        return True


adapter_helper = VirtualTableHelper()