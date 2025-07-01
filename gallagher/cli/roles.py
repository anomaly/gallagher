""" Roles CLI commands

"""

from typing import Optional
from typing_extensions import Annotated

import typer

from rich.console import Console
from rich.table import Table

from .utils import AsyncTyper

from gallagher.enum import SearchSortOrder
from gallagher.cc.roles import Roles

from gallagher.exception import (
    NotFoundException,
)

app = AsyncTyper(
    help="List, query or manage roles"
)


@app.command("list")
async def list():
    """list all roles"""
    console = Console()
    with console.status("[bold green]Fetching roles...", spinner="dots"):
        roles = await Roles.list()

        table = Table(title="Roles")
        for header in roles.cli_header:
            table.add_column(header)

        for row in roles.__rich_repr__():
            table.add_row(*row)

        console.print(table)


@app.command("get")
async def get(
    id: Annotated[int, typer.Argument(help='role id')],
):
    """get a role by id"""
    console = Console()
    with console.status("[bold]Finding role...", spinner="dots"):
        try:
            role = await Roles.retrieve(id)
            [console.print(r) for r in role.__rich_repr__()]
        except NotFoundException as e:
            console.print(f"[bold]No role with id={id} found[/bold]")
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
    """find roles by name"""
    console = Console()
    with console.status("[bold]Searching roles...", spinner="dots"):
        roles = await Roles.search(
            name=name,
            sort=sort,
            top=top,
            division=div,
            direct_division=dirdiv,
            description=description,
        )

        table = Table(title="Roles")
        for header in roles.cli_header:
            table.add_column(header)

        for row in roles.__rich_repr__():
            table.add_row(*row)

        console.print(table)
