""" Cardholder cli commands mounted at ch

"""
import typer
from rich.console import Console
from rich.table import Table

from gallagher.cc.cardholders.cardholders import Cardholder

app = typer.Typer(help="query or manage cardholders")


@app.command("summary")
def summary():
    """ list all cardholders
    """
    import os
    api_key = os.environ.get("GACC_API_KEY")

    from gallagher import cc
    cc.api_key = api_key

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
    typer.echo(f"Getting cardholder {id}")
