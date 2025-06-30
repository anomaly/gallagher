""" Visits CLI commands

"""

from typing import Optional
from typing_extensions import Annotated

import typer

from rich.console import Console
from rich.table import Table

from .utils import AsyncTyper

from gallagher.enum import SearchSortOrder
from gallagher.cc.visits import Visits

from gallagher.exception import (
    NotFoundException,
)

app = AsyncTyper(
    help="List, query or manage visits"
)


@app.command("list")
async def list():
    """list all visits"""
    console = Console()
    with console.status("[bold green]Fetching visits...", spinner="dots"):
        visits = await Visits.list()

        table = Table(title="Visits")
        for header in visits.cli_header:
            table.add_column(header)

        for row in visits.__rich_repr__():
            table.add_row(*row)

        console.print(table)


@app.command("get")
async def get(
    id: Annotated[int, typer.Argument(help='visit id')],
):
    """get a visit by id"""
    console = Console()
    with console.status("[bold]Finding visit...", spinner="dots"):
        try:
            visit = await Visits.retrieve(id)
            [console.print(r) for r in visit.__rich_repr__()]
        except NotFoundException as e:
            console.print(f"[bold]No visit with id={id} found[/bold]")
            raise typer.Exit(code=1)


@app.command("find")
async def find(
    visitor_name: Annotated[
        str,
        typer.Argument(help="Visitor name to search for")
    ],
    sort: Annotated[
        Optional[SearchSortOrder],
        typer.Option(help='Sort order')
    ] = SearchSortOrder.NAME,
    top: Annotated[
        int,
        typer.Option(help='Results to fetch from top')
    ] = 100,
):
    """find visits by visitor name"""
    console = Console()
    with console.status("[bold]Searching visits...", spinner="dots"):
        visits = await Visits.search(
            visitor_name=visitor_name,
            sort=sort,
            top=top,
        )

        table = Table(title="Visits")
        for header in visits.cli_header:
            table.add_column(header)

        for row in visits.__rich_repr__():
            table.add_row(*row)

        console.print(table)
