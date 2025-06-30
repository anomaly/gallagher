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

from .access_groups import app as access_groups_app
from .alarms import app as alarms_app
from .divisions import app as divisions_app
from .cardholders import app as cardholders_app
from .doors import app as doors_app
from .events import app as events_app
from .item import app as items_app
from .azone import app as azone_app
from .agroup import app as agroup_app
from .day import app as day_app
from .door import app as door_app
from .elevator import app as elevator_app
from .fence import app as fence_app
from .ilock import app as ilock_app
from .lockers import app as lockers_app
from .operators import app as operators_app
from .output import app as outputs_app
from .macro import app as macro_app
from .receptions import app as receptions_app
from .roles import app as roles_app
from .schedule import app as schedule_app
from .visits import app as visits_app
from .visitors import app as visitors_app
from .zones import app as zones_app

_help_text = """
gala is a command line interface for the gallagher security command centre.\n
It works by accessing and mutating objects on the command centre via it's\n
JSON API, directly or via the cloud gateway.\n
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
app.add_typer(access_groups_app, name="ag")
app.add_typer(alarms_app, name="alarm")
app.add_typer(divisions_app, name="div")
app.add_typer(cardholders_app, name="ch")
app.add_typer(doors_app, name="door")
app.add_typer(events_app, name="event")
app.add_typer(items_app, name="item")
app.add_typer(azone_app, name="az")
app.add_typer(agroup_app, name="ag")
app.add_typer(day_app, name="day")
app.add_typer(door_app, name="door")
app.add_typer(elevator_app, name="elevator")
app.add_typer(fence_app, name="fence")
app.add_typer(ilock_app, name="ilock")
app.add_typer(lockers_app, name="locker")
app.add_typer(operators_app, name="operator")
app.add_typer(outputs_app, name="output")
app.add_typer(macro_app, name="macro")
app.add_typer(receptions_app, name="reception")
app.add_typer(roles_app, name="role")
app.add_typer(schedule_app, name="schedule")
app.add_typer(visits_app, name="visit")
app.add_typer(visitors_app, name="visitor")
app.add_typer(zones_app, name="zone")

if __name__ == "__main__":
    """In case you are invoking this via Python directly

    This is probably never actually used but it is here for completeness.
    You'd execute this by running `python -m gallagher.cli`
    """
    app()
