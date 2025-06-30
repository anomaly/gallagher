""" Zones CLI commands

"""

from typing import Optional
from typing_extensions import Annotated

import typer

from rich.console import Console
from rich.table import Table

from .utils import AsyncTyper

from gallagher.enum import SearchSortOrder
from gallagher.cc.zones import Zones

from gallagher.exception import (
    NotFoundException,
)

app = AsyncTyper(
    help="List, query or manage zones"
)


@app.command("list")
async def list():
    """list all zones"""
    console = Console()
    with console.status("[bold green]Fetching zones...", spinner="dots"):
        zones = await Zones.list()

        table = Table(title="Zones")
        for header in zones.cli_header:
            table.add_column(header)

        for row in zones.__rich_repr__():
            table.add_row(*row)

        console.print(table)


@app.command("get")
async def get(
    id: Annotated[int, typer.Argument(help='zone id')],
):
    """get a zone by id"""
    console = Console()
    with console.status("[bold]Finding zone...", spinner="dots"):
        try:
            zone = await Zones.retrieve(id)
            [console.print(r) for r in zone.__rich_repr__()]
        except NotFoundException as e:
            console.print(f"[bold]No zone with id={id} found[/bold]")
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
    """find zones by name"""
    console = Console()
    with console.status("[bold]Searching zones...", spinner="dots"):
        zones = await Zones.search(
            name=name,
            sort=sort,
            top=top,
            division=div,
            direct_division=dirdiv,
            description=description,
        )

        table = Table(title="Zones")
        for header in zones.cli_header:
            table.add_column(header)

        for row in zones.__rich_repr__():
            table.add_row(*row)

        console.print(table)
