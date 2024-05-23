""" Divisions

"""

from rich import print as rprint
from rich.console import Console
from rich.table import Table

from .utils import AsyncTyper

from gallagher.cc.alarms.divisions import Division


app = AsyncTyper(
    help="query or modify divisions"
)


@app.command("list")
async def list():
    """list all divisions"""
    console = Console()
    with console.status("[bold green]Fetching divisions...", spinner="clock"):
        divisions = await Division.list()
        table = Table(title="Divisions")
        for header in divisions.cli_header:
            table.add_column(header)

        for row in divisions.__rich_repr__():
            table.add_row(*row)

        console.print(table)


@app.command("get")
async def get(id: int):
    """get a division by id"""
    division = await Division.retrieve(id)
    [rprint(r) for r in division.__rich_repr__()]
