""" Interlock Groups

"""

from typing_extensions import Annotated

import typer

from rich.console import Console
from rich.table import Table

from .utils import AsyncTyper

from gallagher.cc import APIClient
from gallagher.exception import NotFoundException

app = AsyncTyper(help="Query interlock groups on the command centre")


@app.command("list")
async def list(ctx: typer.Context):
    """List all interlock groups"""
    console = Console()
    client: APIClient = ctx.obj["api_client"]

    with console.status("[bold green]Fetching interlock groups...", spinner="dots"):
        interlock_groups = await client.interlock_groups.list()

        table = Table(title="Interlock Groups")
        table.add_column("ID")
        table.add_column("Name")
        table.add_column("Description")

        for ig in interlock_groups.results:
            table.add_row(ig.id, ig.name, ig.description or "")

        console.print(table)


@app.command("get")
async def get(
    ctx: typer.Context,
    id: Annotated[int, typer.Argument(help="interlock group id")],
):
    """Get an interlock group by id"""
    console = Console()
    client: APIClient = ctx.obj["api_client"]

    with console.status("[bold]Finding interlock group...", spinner="dots"):
        try:
            interlock_group = await client.interlock_groups.retrieve(id)
            console.print(interlock_group)
        except NotFoundException:
            console.print(f"[bold]No interlock group with id={id} found[/bold]")
            raise typer.Exit(code=1)
