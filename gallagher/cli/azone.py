""" Alarm Zones

"""

from typing_extensions import Annotated

import typer

from rich.console import Console
from rich.table import Table

from .utils import AsyncTyper

from gallagher.cc import APIClient
from gallagher.exception import NotFoundException

app = AsyncTyper(help="Query alarm zones on the command centre")


@app.command("list")
async def list(ctx: typer.Context):
    """List all alarm zones"""
    console = Console()
    client: APIClient = ctx.obj["api_client"]

    with console.status("[bold green]Fetching alarm zones...", spinner="dots"):
        alarm_zones = await client.alarm_zones.list()

        table = Table(title="Alarm Zones")
        table.add_column("ID")
        table.add_column("Name")
        table.add_column("Description")

        for az in alarm_zones.results:
            table.add_row(az.id, az.name, az.description or "")

        console.print(table)


@app.command("get")
async def get(
    ctx: typer.Context,
    id: Annotated[int, typer.Argument(help="alarm zone id")],
):
    """Get an alarm zone by id"""
    console = Console()
    client: APIClient = ctx.obj["api_client"]

    with console.status("[bold]Finding alarm zone...", spinner="dots"):
        try:
            alarm_zone = await client.alarm_zones.retrieve(id)
            console.print(alarm_zone)
        except NotFoundException:
            console.print(f"[bold]No alarm zone with id={id} found[/bold]")
            raise typer.Exit(code=1)
