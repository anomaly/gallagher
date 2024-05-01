""" Cardholder cli commands mounted at ch

"""
import typer

from rich import print as rprint
from rich.console import Console
from rich.table import Table

from .utils import AsyncTyper

from gallagher.cc.cardholders.cardholders import (
    Cardholder
)

from gallagher.exception import (
    NotFoundException,
)

app = AsyncTyper(
    help="query or manage cardholders"
)


@app.command("list")
async def list():
    """ list all cardholders
    """
    console = Console()
    with console.status(
        "[bold green]Fetching cardholders...",
        spinner="clock"
    ):
        cardholders = await Cardholder.list()

        table = Table(title="Cardholders")
        for header in cardholders.cli_header:
            table.add_column(header)

        for row in cardholders.__rich_repr__():
            table.add_row(*row)

        console.print(table)


@app.command("get")
async def get(id: int):
    """ get a cardholder by id
    """
    try:
        cardholder = await Cardholder.retrieve(id)
        [rprint(r) for r in cardholder.__rich_repr__()]
    except NotFoundException as e:
        rprint(f"[bold]No cardholder with id={id} found[/bold]")
        raise typer.Exit(code=1)
