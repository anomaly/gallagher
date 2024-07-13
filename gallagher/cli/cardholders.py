""" Cardholder cli commands mounted at ch

"""

from typing import Optional
from typing_extensions import Annotated

import typer

from rich.console import Console
from rich.table import Table

from .utils import AsyncTyper

from gallagher.enum import SearchSortOrder
from gallagher.cc.cardholders import Cardholder

from gallagher.exception import (
    NotFoundException,
)

app = AsyncTyper(
    help="List, query or manage or watch changes to cardholders"
)


@app.command("list")
async def list():
    """list all cardholders"""
    console = Console()
    with console.status("[bold green]Fetching cardholders...", spinner="dots"):

        cardholders = await Cardholder.list()

        table = Table(title="Cardholders")
        for header in cardholders.cli_header:
            table.add_column(header)

        for row in cardholders.__rich_repr__():
            table.add_row(*row)

        console.print(table)


@app.command("get")
async def get(
    id: Annotated[int, typer.Argument(help='cardholder id')],
):
    """get a cardholder by id"""
    console = Console()
    with console.status("[bold]Finding cardholder...", spinner="dots"):

        try:
            cardholder = await Cardholder.retrieve(id)
            [console.print(r) for r in cardholder.__rich_repr__()]
        except NotFoundException as e:
            console.print(f"[bold]No cardholder with id={id} found[/bold]")
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
    """find cardholders by name"""
    console = Console()
    with console.status("[bold]Searching cardholders...", spinner="dots"):

        cardholders = await Cardholder.search(
            name=name,
            sort=sort,
            top=top,
            division=div,
            division_dir=dirdiv,
            description=description,
        )

        table = Table(title="Cardholders")
        for header in cardholders.cli_header:
            table.add_column(header)

        for row in cardholders.__rich_repr__():
            table.add_row(*row)

        console.print(table)