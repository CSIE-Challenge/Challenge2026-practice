from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Footer, Header, Static


class MinesweeperApp(App[None]):
    TITLE = "Teaching Minesweeper"
    SUB_TITLE = "Starter project for Git collaboration practice"

    CSS = """
    Screen {
        align: center middle;
    }

    #app-shell {
        width: auto;
        height: auto;
        padding: 1 2;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id="app-shell"):
            yield Static("Minesweeper starter is loading...", id="status")
        yield Footer()


def run() -> None:
    MinesweeperApp().run()


if __name__ == "__main__":
    run()
