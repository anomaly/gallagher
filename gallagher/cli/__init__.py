""" CLI entry point

gal is the gallagher command line, which is constructed using Typer.
At the moment typer does not support async functions, so we have to
use a wrapper to make it work. See utils.py for the AsyncTyper class.

The cli should be pretty self documenting, however see docs/ for
official documentation.
"""
import os

from gallagher import (
    cc,
    __version__
)

from .utils import AsyncTyper

from .alarms import app as alarms_app
from .cardholders import app as cardholders_app

# Load the API key for the package so all entry points
# can use it to query the service
api_key = os.environ.get("GACC_API_KEY")
cc.api_key = api_key

# Main Typer app use to create the CLI
app = AsyncTyper()
# Load up all sub commands
app.add_typer(alarms_app, name="alarms")
app.add_typer(cardholders_app, name="ch")


if __name__ == "__main__":
    """ In case you are invoking this via Python directly

    This is probably never actually used but it is here for completeness.
    You'd execute this by running `python -m gallagher.cli`
    """
    app()
