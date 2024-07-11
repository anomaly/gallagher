""" Alarms CLI

Sub commands to interact with the alarms data

"""

from typing import Optional, List
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

app = AsyncTyper(
    help="List, query, follow, act on alarms in the command centre"
)


@app.command("list")
async def list():
    """list current alarms"""

    console = Console()

    with console.status("[bold green]Fetching alarms...", spinner="dots"):

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
    """get alarm details
    
    These are details of the alarm that are given by the command centre\n
    - Item one\n
    - Items two
    """
    console = Console()
    with console.status("[bold green]Fetching alarm...", spinner="dots"):

        try:
            alarm = await Alarms.retrieve(id)
            [console.print(r) for r in alarm.__rich_repr__()]
        except NotFoundException as e:
            console.print(f"[bold]No alarm with id={id} found[/bold]")
            raise typer.Exit(code=1)

@app.command("history")
async def history(
    id: Annotated[int, typer.Argument(help="alarm id")],
):
    """show history of an alarm"""
    console = Console()

    raise NotImplementedError("Not implemented")

@app.command("tail")
async def tail():
    """watch for alarm updates"""
    console = Console()

    raise NotImplementedError("Not implemented")


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
            alarm_detail = await Alarms.retrieve(id)

            console.log("Adding comment to history ...")
            await Alarms.comment(alarm_detail, message)

            console.print("[green]Comment posted successfully[/green]")

        except NotFoundException as e:
            console.print(f"[red bold]No alarm with id={id} found")
            raise typer.Exit(code=1)


@app.command("ack")
async def acknowledge(
    ids: Annotated[List[int], typer.Argument(help="alarm id")],
    message: Annotated[
        Optional[str],
        typer.Option(
            "-m",
            "--message",
            help="comment to add to history",
        ),
    ] = None,
    yes: Annotated[
        bool,
        typer.Option(
            "-y",
            "--yes",
            help="acknowledge without confirmation",
        )
     ] = False,
):
    """acknowledge an alarm, optionally with a comment"""
    console = Console()

    # ask for confirmation if multiple alarms are to be acknowledged
    if len(ids) > 1 and \
        not yes and \
        not typer.confirm(
            "Are you sure you want to acknowledge multiple alarms?"
        ):
            raise typer.Abort()

    with console.status(
        "[magenta] Acknowledging alarms ...",
    ) as status:
                
        for id in ids:
            try:

                # Get the alarm
                console.log("Finding alarm ...")
                alarm_detail = await Alarms.retrieve(id)

                if not alarm_detail.acknowledge:
                    # alarm has already been acknowledged
                    console.log(
                        f'[red]Alarm {alarm_detail.id} has already been acknowledged[/red]'
                    )
                    continue

                console.log(
                    f'Acknowledging {alarm_detail.id} {"with" if message else "[yellow]without[/yellow]"} comment ...'
                )

                await Alarms.mark_as_acknowledged(alarm_detail, message)
                console.print("[green]Acknowledged alarm[/green]")

            except NotFoundException as e:
                console.print(f"[red bold]No alarm with id={id} found")
                raise typer.Exit(code=1)


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
    with console.status(
        "[magenta] Attempting to view alarm ...",
    ) as status:
        try:

            # Get the alarm
            console.log("Finding alarm ...")
            alarm_detail = await Alarms.retrieve(id)

            if not alarm_detail.view:
                # alarm has already been acknowledged
                console.log(f'[red]Alarm {alarm_detail.id} has already been viewed[/red]')
                raise typer.Exit(code=2)

            console.log(
                f'Marking as viewed {alarm_detail.id} {"with" if message else "[yellow]without[/yellow]"} comment ...')

            await Alarms.mark_as_viewed(alarm_detail, message)
            console.print("[green]Viewed alarm[/green]")


        except NotFoundException as e:
            console.print(f"[red bold]No alarm with id={id} found")
            raise typer.Exit(code=1)


@app.command("process")
async def acknowledge(
    ids: Annotated[List[int], typer.Argument(help="alarm id")],
    message: Annotated[
        Optional[str],
        typer.Option(
            "-m",
            "--message",
            help="comment to add to history",
        ),
    ] = None,
    yes: Annotated[
        bool,
        typer.Option(
            "-y",
            "--yes",
            help="acknowledge without confirmation",
        )
     ] = False,
):
    """mark alarm as processed, optionally with a comment"""
    console = Console()
    # ask for confirmation if multiple alarms are to be acknowledged
    if len(ids) > 1 and \
        not yes and \
        not typer.confirm(
            "Are you sure you want to process multiple alarms?"
        ):
            raise typer.Abort()

    with console.status(
        "[magenta] Processing alarms ...",
    ) as status:
        
        for id in ids:
            try:

                # Get the alarm
                console.log("Finding alarm ...")
                alarm_detail = await Alarms.retrieve(id)

                if not alarm_detail.process:
                    # alarm has already been acknowledged
                    console.log(
                        f'[red]Alarm {alarm_detail.id} has already been processed[/red]'
                    )
                    continue

                console.log(
                    f'Processing {alarm_detail.id} {"with" if message else "[yellow]without[/yellow]"} comment ...'
                )

                await Alarms.mark_as_processed(alarm_detail, message)
                console.print("[green]Processed alarm[/green]")

            except NotFoundException as e:
                console.print(f"[red bold]No alarm with id={id} found")
                raise typer.Exit(code=1)
