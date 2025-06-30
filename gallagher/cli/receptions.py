""" Receptions CLI commands

"""

from typing import Optional
from typing_extensions import Annotated

import typer

from rich.console import Console
from rich.table import Table

from .utils import AsyncTyper

from gallagher.enum import SearchSortOrder
from gallagher.cc.receptions import Receptions

from gallagher.exception import (
    NotFoundException,
)

app = AsyncTyper(
    help="List, query or manage receptions"
)


@app.command("list")
async def list():
    """list all receptions"""
    console = Console()
    with console.status("[bold green]Fetching receptions...", spinner="dots"):
        receptions = await Receptions.list()

        table = Table(title="Receptions")
        for header in receptions.cli_header:
            table.add_column(header)

        for row in receptions.__rich_repr__():
            table.add_row(*row)

        console.print(table)


@app.command("get")
async def get(
    id: Annotated[int, typer.Argument(help='reception id')],
):
    """get a reception by id"""
    console = Console()
    with console.status("[bold]Finding reception...", spinner="dots"):
        try:
            reception = await Receptions.retrieve(id)
            [console.print(r) for r in reception.__rich_repr__()]
        except NotFoundException as e:
            console.print(f"[bold]No reception with id={id} found[/bold]")
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
    """find receptions by name"""
    console = Console()
    with console.status("[bold]Searching receptions...", spinner="dots"):
        receptions = await Receptions.search(
            name=name,
            sort=sort,
            top=top,
            division=div,
            direct_division=dirdiv,
            description=description,
        )

        table = Table(title="Receptions")
        for header in receptions.cli_header:
            table.add_column(header)

        for row in receptions.__rich_repr__():
            table.add_row(*row)

        console.print(table)
