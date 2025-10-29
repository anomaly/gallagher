""" Visitors CLI commands

"""

from typing import Optional
from typing_extensions import Annotated

import typer

from rich.console import Console
from rich.table import Table

from .utils import AsyncTyper

from gallagher.enum import SearchSortOrder
from gallagher.cc.visitors import Visitors

from gallagher.exception import (
    NotFoundException,
)

app = AsyncTyper(
    help="List, query or manage visitors"
)


@app.command("list")
async def list():
    """list all visitors"""
    console = Console()
    with console.status("[bold green]Fetching visitors...", spinner="dots"):
        visitors = await Visitors.list()

        table = Table(title="Visitors")
        for header in visitors.cli_header:
            table.add_column(header)

        for row in visitors.__rich_repr__():
            table.add_row(*row)

        console.print(table)


@app.command("get")
async def get(
    id: Annotated[int, typer.Argument(help='visitor id')],
):
    """get a visitor by id"""
    console = Console()
    with console.status("[bold]Finding visitor...", spinner="dots"):
        try:
            visitor = await Visitors.retrieve(id)
            [console.print(r) for r in visitor.__rich_repr__()]
        except NotFoundException as e:
            console.print(f"[bold]No visitor with id={id} found[/bold]")
            raise typer.Exit(code=1)


@app.command("find")
async def find(
    name: Annotated[
        str,
        typer.Argument(help="First or last name to search for")
    ],
    sort: Annotated[
        Optional[SearchSortOrder],
        typer.Option(help='Sort order')
    ] = SearchSortOrder.NAME,
    top: Annotated[
        int,
        typer.Option(help='Results to fetch from top')
    ] = 100,
    div: Annotated[
        Optional[int],
        typer.Option(help='Division id for hierarchical search')
    ] = None,
    dirdiv: Annotated[
        Optional[int],
        typer.Option(
            '--ddiv',
            help='Division id for direct search'
        )
    ] = None,
):
    """find visitors by name"""
    console = Console()
    with console.status("[bold]Searching visitors...", spinner="dots"):
        visitors = await Visitors.search(
            name=name,
            sort=sort,
            top=top,
            division=div,
            direct_division=dirdiv,
        )

        table = Table(title="Visitors")
        for header in visitors.cli_header:
            table.add_column(header)

        for row in visitors.__rich_repr__():
            table.add_row(*row)

        console.print(table)
