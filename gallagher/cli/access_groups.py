""" Access Groups CLI commands

"""

from typing import Optional
from typing_extensions import Annotated

import typer

from rich.console import Console
from rich.table import Table

from .utils import AsyncTyper

from gallagher.enum import SearchSortOrder
from gallagher.cc.access_groups import AccessGroups

from gallagher.exception import (
    NotFoundException,
)

app = AsyncTyper(
    help="List, query or manage access groups"
)


@app.command("list")
async def list():
    """list all access groups"""
    console = Console()
    with console.status("[bold green]Fetching access groups...", spinner="dots"):
        access_groups = await AccessGroups.list()

        table = Table(title="Access Groups")
        for header in access_groups.cli_header:
            table.add_column(header)

        for row in access_groups.__rich_repr__():
            table.add_row(*row)

        console.print(table)


@app.command("get")
async def get(
    id: Annotated[int, typer.Argument(help='access group id')],
):
    """get an access group by id"""
    console = Console()
    with console.status("[bold]Finding access group...", spinner="dots"):
        try:
            access_group = await AccessGroups.retrieve(id)
            [console.print(r) for r in access_group.__rich_repr__()]
        except NotFoundException as e:
            console.print(f"[bold]No access group with id={id} found[/bold]")
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
    """find access groups by name"""
    console = Console()
    with console.status("[bold]Searching access groups...", spinner="dots"):
        access_groups = await AccessGroups.search(
            name=name,
            sort=sort,
            top=top,
            division=div,
            direct_division=dirdiv,
            description=description,
        )

        table = Table(title="Access Groups")
        for header in access_groups.cli_header:
            table.add_column(header)

        for row in access_groups.__rich_repr__():
            table.add_row(*row)

        console.print(table)
