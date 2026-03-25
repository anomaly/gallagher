""" Fence Zones

"""

from typing_extensions import Annotated

import typer

from rich.console import Console
from rich.table import Table

from .utils import AsyncTyper

from gallagher.cc import APIClient
from gallagher.exception import NotFoundException

app = AsyncTyper(help="Query fence zones on the command centre")


@app.command("list")
async def list(ctx: typer.Context):
    """List all fence zones"""
    console = Console()
    client: APIClient = ctx.obj["api_client"]

    with console.status("[bold green]Fetching fence zones...", spinner="dots"):
        fence_zones = await client.fence_zones.list()

        table = Table(title="Fence Zones")
        table.add_column("ID")
        table.add_column("Name")
        table.add_column("Description")

        for fz in fence_zones.results:
            table.add_row(fz.id, fz.name, fz.description or "")

        console.print(table)


@app.command("get")
async def get(
    ctx: typer.Context,
    id: Annotated[int, typer.Argument(help="fence zone id")],
):
    """Get a fence zone by id"""
    console = Console()
    client: APIClient = ctx.obj["api_client"]

    with console.status("[bold]Finding fence zone...", spinner="dots"):
        try:
            fence_zone = await client.fence_zones.retrieve(id)
            console.print(fence_zone)
        except NotFoundException:
            console.print(f"[bold]No fence zone with id={id} found[/bold]")
            raise typer.Exit(code=1)
