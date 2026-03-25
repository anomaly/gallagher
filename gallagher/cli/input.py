""" Inputs

"""

from typing_extensions import Annotated

import typer

from rich.console import Console
from rich.table import Table

from .utils import AsyncTyper

from gallagher.cc import APIClient
from gallagher.exception import NotFoundException

app = AsyncTyper(help="Query inputs on the command centre")


@app.command("list")
async def list(ctx: typer.Context):
    """List all inputs"""
    console = Console()
    client: APIClient = ctx.obj["api_client"]

    with console.status("[bold green]Fetching inputs...", spinner="dots"):
        inputs = await client.inputs.list()

        table = Table(title="Inputs")
        table.add_column("ID")
        table.add_column("Name")
        table.add_column("Status")

        for i in inputs.results:
            table.add_row(i.id, i.name, i.status or "")

        console.print(table)


@app.command("get")
async def get(
    ctx: typer.Context,
    id: Annotated[int, typer.Argument(help="input id")],
):
    """Get an input by id"""
    console = Console()
    client: APIClient = ctx.obj["api_client"]

    with console.status("[bold]Finding input...", spinner="dots"):
        try:
            inp = await client.inputs.retrieve(id)
            console.print(inp)
        except NotFoundException:
            console.print(f"[bold]No input with id={id} found[/bold]")
            raise typer.Exit(code=1)
