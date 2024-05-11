""" Adapter and SQLAlchemy dialect for shillelagh

The package provides extensions to provide a SQL interface for the
Gallagher API.

[shillelagh](https://github.com/betodealmeida/shillelagh)
"""

from typing import Any, Dict, Iterator, List, Optional, Tuple


class GallagherCommandCentreAPI(Adapter):

    # The adapter doesn't access the filesystem.
    safe = True

    # The adapter will receive a ``limit`` argument in the ``get_data``
    # method, and will be responsible for limiting the number of rows returned.
    supports_limit = True

    supports_offset = False

    # Check to see if we can do this using the partial column feature
    supports_requested_columns = False

    @staticmethod
    def supports(uri: str, fast: bool = True, **kwargs: Any) -> Optional[bool]:
        return False

    @staticmethod
    def parse_uri(uri: str) -> Tuple[str]:
        return (uri,)

    def __init__(self, uri: str):
        super().__init__()
        self.uri = uri
