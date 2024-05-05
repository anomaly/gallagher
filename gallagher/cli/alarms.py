""" Alarms CLI

Sub commands to interact with the alarms data

"""

from typing import Optional
from typing_extensions import Annotated

import typer

from .utils import AsyncTyper

app = AsyncTyper(
    help="list or query alarms in the command centre"
)


@app.command("list")
async def list():
    """ list current alarms
    """
    console = Console()
    with console.status(
        "[bold green]Fetching divisions...",
        spinner="clock"
    ):
        divisions = await Division.list()
        table = Table(title="Divisions")
        for header in divisions.cli_header:
            table.add_column(header)

        for row in divisions.__rich_repr__():
            table.add_row(*row)

        console.print(table)


@app.command("get")
async def get(
    id: Annotated[
        int,
        typer.Argument(help="alarm id")
    ],
):
    """ get alarm details
    """
    console = Console()


@app.command("comment")
async def comment(
    id: Annotated[int, typer.Argument(help="alarm id")],
    comment: Annotated[
        str,
        typer.Option(help="comment to add to history"
    )],
):
    """ comment on an alarm
    """
    console = Console()


@app.command("ack")
async def acknowledge(
    id: Annotated[int, typer.Argument(help="alarm id")],
    comment: Annotated[
        Optional[str],
        typer.Option(help="comment to add to history")
    ] = None,
):
    """ acknowledge an alarm, optionally with a comment
    """
    console = Console()


@app.command("view")
async def acknowledge(
    id: Annotated[int, typer.Argument(help="alarm id")],
    comment: Annotated[
        Optional[str],
        typer.Option(help="comment to add to history")
    ] = None,
):
    """ mark alarm as viewed, optionally with a comment
    """
    console = Console()


@app.command("process")
async def acknowledge(
    id: Annotated[int, typer.Argument(help="alarm id")],
    comment: Annotated[
        Optional[str],
        typer.Option(help="comment to add to history")
    ] = None,
):
    """ mark alarm as processed, optionally with a comment
    """
    console = Console()
