""" Operators CLI commands

"""

from typing import Optional
from typing_extensions import Annotated

import typer

from rich.console import Console
from rich.table import Table

from .utils import AsyncTyper

from gallagher.enum import SearchSortOrder
from gallagher.cc.operators import Operators

from gallagher.exception import (
    NotFoundException,
)

app = AsyncTyper(
    help="List, query or manage operators"
)


@app.command("list")
async def list():
    """list all operators"""
    console = Console()
    with console.status("[bold green]Fetching operators...", spinner="dots"):
        operators = await Operators.list()

        table = Table(title="Operators")
        for header in operators.cli_header:
            table.add_column(header)

        for row in operators.__rich_repr__():
            table.add_row(*row)

        console.print(table)


@app.command("get")
async def get(
    id: Annotated[int, typer.Argument(help='operator id')],
):
    """get an operator by id"""
    console = Console()
    with console.status("[bold]Finding operator...", spinner="dots"):
        try:
            operator = await Operators.retrieve(id)
            [console.print(r) for r in operator.__rich_repr__()]
        except NotFoundException as e:
            console.print(f"[bold]No operator with id={id} found[/bold]")
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
    """find operators by name"""
    console = Console()
    with console.status("[bold]Searching operators...", spinner="dots"):
        operators = await Operators.search(
            name=name,
            sort=sort,
            top=top,
            division=div,
            direct_division=dirdiv,
            description=description,
        )

        table = Table(title="Operators")
        for header in operators.cli_header:
            table.add_column(header)

        for row in operators.__rich_repr__():
            table.add_row(*row)

        console.print(table)
