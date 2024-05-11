""" Dashboard

Where you land up once the tui is started via the command line
this shows you some statistics, and health information.
"""

from textual.app import ComposeResult

from textual.containers import (
    Container,
    Grid,
)

from textual.widgets import (
    Digits,
    Placeholder,
)


class Dashboard(Container):

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        with Grid():
            yield Placeholder("Dashboard")
            yield Digits("3.141,592,653,5897", id="pi")
