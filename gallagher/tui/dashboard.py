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
    DataTable,
)

ROWS = [
    ("lane", "swimmer", "country", "time"),
    (4, "Joseph Schooling", "Singapore", 50.39),
    (2, "Michael Phelps", "United States", 51.14),
    (5, "Chad le Clos", "South Africa", 51.14),
    (6, "László Cseh", "Hungary", 51.14),
    (3, "Li Zhuhao", "China", 51.26),
    (8, "Mehdy Metella", "France", 51.58),
    (7, "Tom Shields", "United States", 51.73),
    (1, "Aleksandr Sadovnikov", "Russia", 51.84),
    (10, "Darren Burns", "Scotland", 51.84),
]


class VisitTimelineWidget(Container):

    def compose(self) -> ComposeResult:
        yield DataTable()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns(*ROWS[0])
        table.add_rows(ROWS[1:])

    # def compose(self) -> ComposeResult:
    #     """Visit timeline widget"""
    #     with Grid():
    #         yield Placeholder("Visit Timeline, changes")

class Dashboard(Container):

    CSS_PATH = "gallagher.tcss"

    def compose(self) -> ComposeResult:
        """Dashboard for the command centre"""
        with Grid():
            yield VisitTimelineWidget()