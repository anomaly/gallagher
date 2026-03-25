""" Competencies

"""

from typing_extensions import Annotated

import typer

from rich.console import Console
from rich.table import Table

from .utils import AsyncTyper

from gallagher.cc import APIClient
from gallagher.exception import NotFoundException

app = AsyncTyper(help="Query competencies on the command centre")


@app.command("list")
async def list(ctx: typer.Context):
    """List all competencies"""
    console = Console()
    client: APIClient = ctx.obj["api_client"]

    with console.status("[bold green]Fetching competencies...", spinner="dots"):
        competencies = await client.competencies.list()

        table = Table(title="Competencies")
        table.add_column("ID")
        table.add_column("Name")
        table.add_column("Description")

        for c in competencies.results:
            table.add_row(c.id, c.name, c.description or "")

        console.print(table)


@app.command("get")
async def get(
    ctx: typer.Context,
    id: Annotated[int, typer.Argument(help="competency id")],
):
    """Get a competency by id"""
    console = Console()
    client: APIClient = ctx.obj["api_client"]

    with console.status("[bold]Finding competency...", spinner="dots"):
        try:
            competency = await client.competencies.retrieve(id)
            console.print(competency)
        except NotFoundException:
            console.print(f"[bold]No competency with id={id} found[/bold]")
            raise typer.Exit(code=1)
