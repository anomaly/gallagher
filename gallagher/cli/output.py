""" Outputs

"""

from typing_extensions import Annotated

import typer

from rich.console import Console
from rich.table import Table

from .utils import AsyncTyper

from gallagher.cc import APIClient
from gallagher.exception import NotFoundException

app = AsyncTyper(help="Query outputs on the command centre")


@app.command("list")
async def list(ctx: typer.Context):
    """List all outputs"""
    console = Console()
    client: APIClient = ctx.obj["api_client"]

    with console.status("[bold green]Fetching outputs...", spinner="dots"):
        outputs = await client.outputs.list()

        table = Table(title="Outputs")
        table.add_column("ID")
        table.add_column("Name")
        table.add_column("Status")

        for o in outputs.results:
            table.add_row(o.id, o.name, o.status or "")

        console.print(table)


@app.command("get")
async def get(
    ctx: typer.Context,
    id: Annotated[int, typer.Argument(help="output id")],
):
    """Get an output by id"""
    console = Console()
    client: APIClient = ctx.obj["api_client"]

    with console.status("[bold]Finding output...", spinner="dots"):
        try:
            output = await client.outputs.retrieve(id)
            console.print(output)
        except NotFoundException:
            console.print(f"[bold]No output with id={id} found[/bold]")
            raise typer.Exit(code=1)
