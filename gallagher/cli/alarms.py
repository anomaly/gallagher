""" Alarms CLI

Sub commands to interact with the alarms data

"""

from typing import Optional
from typing_extensions import Annotated

import typer

from rich.console import Console
from rich.progress import Progress, TaskID
from rich.table import Table

from .utils import AsyncTyper

from ..exception import (
    NotFoundException,
)

from gallagher.cc.alarms import (
    Alarms,
)

app = AsyncTyper(help="list or query alarms in the command centre")


@app.command("list")
async def list():
    """list current alarms"""
    console = Console()
    with console.status("[bold green]Fetching alarms...", spinner="clock"):
        alarms = await Alarms.list()
        table = Table(title="Alarms")
        for header in alarms.cli_header:
            table.add_column(header)

        for row in alarms.__rich_repr__():
            table.add_row(*row)

        console.print(table)


@app.command("get")
async def get(
    id: Annotated[int, typer.Argument(help="alarm id")],
):
    """get alarm details"""
    console = Console()


@app.command("comment")
async def comment(
    id: Annotated[int, typer.Argument(help="alarm id")],
    message: Annotated[
        str,
        typer.Option(
            "-m",
            "--message",
            help="comment to add to history",
        ),
    ],
):
    """comment on an alarm"""
    console = Console()
    with console.status(
        "[magenta] Commenting on alarm ...",
    ) as status:
        try:
            console.log("Finding alarm ...")
            comment_detail = await Alarms.retrieve(id)
            console.log("Adding comment to history ...")
            await Alarms.comment(comment_detail, message)
            console.print("[green]Comment posted successfully[/green]")
        except NotFoundException as e:
            console.print(f"[red bold]No alarm with id={id} found")
            raise typer.Exit(code=1)


@app.command("ack")
async def acknowledge(
    id: Annotated[int, typer.Argument(help="alarm id")],
    message: Annotated[
        Optional[str],
        typer.Option(
            "-m",
            "--message",
            help="comment to add to history",
        ),
    ] = None,
):
    """acknowledge an alarm, optionally with a comment"""
    console = Console()


@app.command("view")
async def acknowledge(
    id: Annotated[int, typer.Argument(help="alarm id")],
    message: Annotated[
        Optional[str],
        typer.Option(
            "-m",
            "--message",
            help="comment to add to history",
        ),
    ] = None,
):
    """mark alarm as viewed, optionally with a comment"""
    console = Console()


@app.command("process")
async def acknowledge(
    id: Annotated[int, typer.Argument(help="alarm id")],
    message: Annotated[
        Optional[str],
        typer.Option(
            "-m",
            "--message",
            help="comment to add to history",
        ),
    ] = None,
):
    """mark alarm as processed, optionally with a comment"""
    console = Console()
