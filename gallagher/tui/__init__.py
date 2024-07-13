""" Console
"""

from textual.app import App, ComposeResult

from textual.screen import (
    ModalScreen,
)

from textual.containers import (
    Container,
    Horizontal,
    Grid,
)

from textual.widgets import (
    Header,
    Footer,
    Placeholder,
)

from .dashboard import Dashboard

class ModalScreen(ModalScreen):

    def compose(self) -> ComposeResult:
        # Make a two column grid and occupy the second half
        # with a placeholder
        with Container():
            # yield Container()
            yield Placeholder("This is a modal screen")

class GallagherConsole(App):
    """A console interface for the Gallagher Command Centre."""

    CSS_PATH = "gallagher.tcss"

    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"), 
        ("ctrl+q", "quit", "Quit")
    ]

    # Decorative constants
    TITLE = "Gallagher"
    SUB_TITLE = "power tools for gallagher"

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header(show_clock=True)
        yield Dashboard()
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark

    def key_m(self) -> None:
        """Open the modal screen."""
        self.push_screen(ModalScreen())


# Move this out side of __main__ so that textual cli
# and python can find them as instance variables
#
# see service.tom and you can run this via the terminal
# textual-web --config serve.toml 
# to get a web interface, follow textual-web for further
# development and how we can use it provide a demo
app = GallagherConsole()

def main():
    app.run()

if __name__ == "__main__":
    main()
