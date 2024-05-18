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


class VisitTimelineWidget(Container):

    def compose(self) -> ComposeResult:
        """Visit timeline widget"""
        with Grid():
            yield Placeholder("Visit Timeline, changes")

class Dashboard(Container):

    def compose(self) -> ComposeResult:
        """Dashboard for the command centre"""
        with Grid():
            yield VisitTimelineWidget()