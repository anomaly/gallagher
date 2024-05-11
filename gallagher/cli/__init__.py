""" CLI entry point

gal is the gallagher command line, which is constructed using Typer.
At the moment typer does not support async functions, so we have to
use a wrapper to make it work. See utils.py for the AsyncTyper class.

The cli should be pretty self documenting, however see docs/ for
official documentation.
"""

import os

from gallagher import cc, __version__

from .utils import AsyncTyper

from .alarms import app as alarms_app
from .divisions import app as divisions_app
from .cardholders import app as cardholders_app
from .events import app as events_app

_help_text = """
gala is a command line interface for the gallagher security command centre.\n
It works by accessing and mutating objects on the command centre via it's\n
JSON REST like API, directly or via the cloud gateway.\n
\n
It's intent it to make available scriptable endpoints to ease automation.
"""

# Load the API key for the package so all entry points
# can use it to query the service
api_key = os.environ.get("GACC_API_KEY")
cc.api_key = api_key

# Main Typer app use to create the CLI
app = AsyncTyper(
    help=_help_text,
)

# Load up all sub commands
app.add_typer(alarms_app, name="alarm")
app.add_typer(divisions_app, name="div")
app.add_typer(cardholders_app, name="ch")
app.add_typer(events_app, name="event")

if __name__ == "__main__":
    """In case you are invoking this via Python directly

    This is probably never actually used but it is here for completeness.
    You'd execute this by running `python -m gallagher.cli`
    """
    app()
