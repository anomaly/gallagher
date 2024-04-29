""" Alarms CLI

Sub commands to interact with the alarms data

"""


from .utils import AsyncTyper


app = AsyncTyper(
    help="list or query alarms in the command centre"
)


@app.command("list")
async def list():
    """ list all divisions
    """
    console = Console()
    with console.status(
        "[bold green]Fetching divisions...",
        spinner="clock"
    ):
        divisions = await Division.list()
        table = Table(title="Divisions")
        for header in divisions.cli_header:
            table.add_column(header)

        for row in divisions.__rich_repr__():
            table.add_row(*row)

        console.print(table)
