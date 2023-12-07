""" Cardholder cli commands mounted at ch

"""
import typer
from rich import print as rprint
from rich.console import Console
from rich.table import Table

from gallagher.cc.cardholders.cardholders import Cardholder

app = typer.Typer(help="query or manage cardholders")


@app.command("summary")
def summary():
    """ list all cardholders
    """
    cardholders = Cardholder.list()

    table = Table(title="Cardholders")
    for header in cardholders.cli_header:
        table.add_column(header)

    for row in cardholders.cli_repr:
        table.add_row(*row)

    console = Console()
    console.print(table)


@app.command("get")
def get(id: int):
    """ get a cardholder by id
    """
    cardholder = Cardholder.retrieve(id)
    rprint(cardholder.__dict__)
