""" Doors CLI commands

"""

from typing import Optional
from typing_extensions import Annotated

import typer

from rich.console import Console
from rich.table import Table

from .utils import AsyncTyper

from gallagher.enum import SearchSortOrder
from gallagher.cc.doors import Doors

from gallagher.exception import (
    NotFoundException,
)

app = AsyncTyper(
    help="List, query or manage doors"
)


@app.command("list")
async def list():
    """list all doors"""
    console = Console()
    with console.status("[bold green]Fetching doors...", spinner="dots"):
        doors = await Doors.list()

        table = Table(title="Doors")
        for header in doors.cli_header:
            table.add_column(header)

        for row in doors.__rich_repr__():
            table.add_row(*row)

        console.print(table)


@app.command("get")
async def get(
    id: Annotated[int, typer.Argument(help='door id')],
):
    """get a door by id"""
    console = Console()
    with console.status("[bold]Finding door...", spinner="dots"):
        try:
            door = await Doors.retrieve(id)
            [console.print(r) for r in door.__rich_repr__()]
        except NotFoundException as e:
            console.print(f"[bold]No door with id={id} found[/bold]")
            raise typer.Exit(code=1)


@app.command("find")
async def find(
    name: Annotated[
        str,
        typer.Argument(help="Name to search for")
    ],
    sort: Annotated[
        Optional[SearchSortOrder],
        typer.Option(help='Sort order')
    ] = SearchSortOrder.NAME,
    description: Annotated[
        Optional[str],
        typer.Option(
            '--desc',
            help='Keywords to search in description'
        )
    ] = None,
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
    """find doors by name"""
    console = Console()
    with console.status("[bold]Searching doors...", spinner="dots"):
        doors = await Doors.search(
            name=name,
            sort=sort,
            top=top,
            division=div,
            direct_division=dirdiv,
            description=description,
        )

        table = Table(title="Doors")
        for header in doors.cli_header:
            table.add_column(header)

        for row in doors.__rich_repr__():
            table.add_row(*row)

        console.print(table)
