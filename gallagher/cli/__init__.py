""" CLI entry point

gal is the gallagher command line, which is constructed using Typer.
At the moment typer does not support async functions, so we have to
use a wrapper to make it work. See utils.py for the AsyncTyper class.

The cli should be pretty self documenting, however see docs/ for
official documentation.
"""

import typer
import click

from gallagher import __version__

from gallagher.cc import APIClient, CommandCentreConfig
from gallagher.const import URL

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

# Main Typer app use to create the CLI
app = AsyncTyper(
    help=_help_text,
)

# Global parameters
@app.callback()
def main(
    ctx: click.Context,
    api_key: str = typer.Option(
        None,
        "--api-key",
        "-k",
        envvar="GACC_API_KEY",
        prompt_required=True,
        help="API key for authentication"
    ),
    tls_cert: str = typer.Option(
        None,
        "--tls-cert",
        "-c",
        envvar="GACC_TLS_CERT",
        help="Path to TLS certificate file"
    ),
    tls_key: str = typer.Option(
        None,
        "--tls-key",
        envvar="GACC_TLS_KEY",
        help="Path to TLS private key file"
    ),
    proxy_url: str = typer.Option(
        None,
        "--proxy-url",
        "-p",
        envvar="GACC_PROXY_URL",
        help="Proxy URL for HTTP requests"
    ),
    use_basic_auth: bool = typer.Option(
        False,
        "--use-basic-auth",
        "-b",
        envvar="GACC_USE_BASIC_AUTH",
        help="Use basic authentication instead of API key"
    ),
    gateway: str = typer.Option(
        "AU",
        "--gateway",
        "-g",
        envvar="GACC_GATEWAY",
        help="Gateway region (AU or US)",
        click_type=click.Choice(["AU", "US"], case_sensitive=False)
    ),
    output_format: str = typer.Option(
        "pretty",
        "--format",
        "-f",
        help="Output format",
        click_type=click.Choice(["pretty", "json", "csv", "markdown"], case_sensitive=False)
    ),
):
    """Main callback to handle global parameters.
    
    The API client is initialised here and is passed to subcommands via
    dependency injection.
    """
    ctx.ensure_object(dict)
    ctx.obj['output_format'] = output_format

    config = CommandCentreConfig(
        api_key=api_key,
        file_tls_certificate=tls_cert,
        file_tls_key=tls_key,
        proxy=proxy_url,
        use_basic_authentication=use_basic_auth,
        api_base=(gateway == "US" and URL.CLOUD_GATEWAY_US) \
            or URL.CLOUD_GATEWAY_AU,
    )

    ctx.obj['api_client'] = APIClient(config)


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

