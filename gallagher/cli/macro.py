""" Macros

"""

from typing_extensions import Annotated

import typer

from rich.console import Console
from rich.table import Table

from .utils import AsyncTyper

from gallagher.cc import APIClient
from gallagher.exception import NotFoundException

app = AsyncTyper(help="Query macros on the command centre")


@app.command("list")
async def list(ctx: typer.Context):
    """List all macros"""
    console = Console()
    client: APIClient = ctx.obj["api_client"]

    with console.status("[bold green]Fetching macros...", spinner="dots"):
        macros = await client.macros.list()

        table = Table(title="Macros")
        table.add_column("ID")
        table.add_column("Name")
        table.add_column("Description")

        for m in macros.results:
            table.add_row(m.id, m.name, m.description or "")

        console.print(table)


@app.command("get")
async def get(
    ctx: typer.Context,
    id: Annotated[int, typer.Argument(help="macro id")],
):
    """Get a macro by id"""
    console = Console()
    client: APIClient = ctx.obj["api_client"]

    with console.status("[bold]Finding macro...", spinner="dots"):
        try:
            macro = await client.macros.retrieve(id)
            console.print(macro)
        except NotFoundException:
            console.print(f"[bold]No macro with id={id} found[/bold]")
            raise typer.Exit(code=1)
