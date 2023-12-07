""" Alarms


"""

from gallagher import cc
import os
import typer

api_key = os.environ.get("GACC_API_KEY")

cc.api_key = api_key

app = typer.Typer()
