""" Elevator Groups

"""

from typing_extensions import Annotated

import typer

from rich.console import Console
from rich.table import Table

from .utils import AsyncTyper

from gallagher.cc import APIClient
from gallagher.exception import NotFoundException

app = AsyncTyper(help="Query elevator groups on the command centre")


@app.command("list")
async def list(ctx: typer.Context):
    """List all elevator groups"""
    console = Console()
    client: APIClient = ctx.obj["api_client"]

    with console.status("[bold green]Fetching elevator groups...", spinner="dots"):
        elevators = await client.elevators.list()

        table = Table(title="Elevator Groups")
        table.add_column("ID")
        table.add_column("Name")
        table.add_column("Description")

        for e in elevators.results:
            table.add_row(e.id, e.name, e.description or "")

        console.print(table)


@app.command("get")
async def get(
    ctx: typer.Context,
    id: Annotated[int, typer.Argument(help="elevator group id")],
):
    """Get an elevator group by id"""
    console = Console()
    client: APIClient = ctx.obj["api_client"]

    with console.status("[bold]Finding elevator group...", spinner="dots"):
        try:
            elevator = await client.elevators.retrieve(id)
            console.print(elevator)
        except NotFoundException:
            console.print(f"[bold]No elevator group with id={id} found[/bold]")
            raise typer.Exit(code=1)
