"""" Gallagher Python idiomatic client

 Copyright (c) 2025, Anomaly Software Pty Ltd

 This project is **NOT** officially affiliated with Gallagher Security.

 Distributed under the terms of the MIT License.
"""

# Assumed we are running Python 3.8 or later
# https://docs.python.org/3.8/library/importlib.metadata.html
from importlib.metadata import version, PackageNotFoundError
__package_name__ = __name__.split(".", 1)[0]

try:
    __version__ = version(__package_name__)
except PackageNotFoundError:
    __version__ = "0.0.0"  # fallback for local dev