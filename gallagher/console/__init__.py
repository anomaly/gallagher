""" Console 
"""

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer


class GallagherConsole(App):
    """A Textual app to manage stopwatches."""

    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode")
    ]

    def on_mount(self) -> None:
        self.title = "Gallagher"
        self.sub_title = "Super charged textual console"

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark


def main():
    app = GallagherConsole()
    app.run()


if __name__ == "__main__":
    main()
