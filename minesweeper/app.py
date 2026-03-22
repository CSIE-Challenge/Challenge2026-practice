from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Footer, Header, Static

from minesweeper.game.state import GameState
from minesweeper.ui.board_view import BoardView


class MinesweeperApp(App[None]):
    TITLE = "Teaching Minesweeper"
    SUB_TITLE = "Starter project for Git collaboration practice"

    CSS = """
    Screen {
        background: $background;
        color: $foreground;
        align: center middle;
    }

    #app-shell {
        width: 1fr;
        height: 1fr;
        padding: 1 2 2 2;
    }

    #chrome {
        width: 1fr;
        max-width: 96;
        height: auto;
        margin: 0;
    }

    #hero {
        width: 1fr;
        padding: 0 1 0 1;
        color: $foreground;
        text-style: bold;
    }

    #subtitle {
        width: 1fr;
        padding: 0 1 1 1;
        color: #a7b4c8;
    }

    #workspace {
        width: 1fr;
        height: auto;
        align: center top;
    }

    .panel {
        border: round $panel;
        background: $surface;
        padding: 1;
    }

    #board-panel {
        width: auto;
        margin-right: 2;
    }

    #side-panel {
        width: 26;
        min-width: 26;
    }

    .panel-title {
        color: $primary;
        text-style: bold;
        padding: 0 1 1 1;
    }

    #status {
        border: round $secondary;
        background: $panel;
        color: $foreground;
        padding: 1 1;
        margin-bottom: 1;
    }

    #tips {
        color: #c7d0dd;
        margin-bottom: 1;
        padding: 0 1;
    }

    #legend {
        color: #d8dee9;
        padding: 0 1;
    }
    """

    def __init__(self) -> None:
        super().__init__()
        self.theme = "nord"
        self.game_state = GameState()

    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id="app-shell"):
            with Vertical(id="chrome"):
                yield Static("Minesweeper Starter", id="hero")
                yield Static(
                    "Textual starter project for branch, PR, merge, and conflict practice.",
                    id="subtitle",
                )
                with Horizontal(id="workspace"):
                    with Vertical(id="board-panel", classes="panel"):
                        yield Static("Board", classes="panel-title")
                        yield BoardView(self.game_state)
                    with Vertical(id="side-panel", classes="panel"):
                        yield Static("Status", classes="panel-title")
                        yield Static(self.game_state.status_text, id="status")
                        yield Static(
                            "Left click reveals one cell.\nSeveral features are intentionally incomplete.",
                            id="tips",
                        )
                        yield Static(
                            "Legend\n"
                            "blank = hidden or empty\n"
                            "1-8 = adjacent mines\n"
                            "* = revealed mine",
                            id="legend",
                        )
        yield Footer()

    def on_board_view_changed(self, message: BoardView.Changed) -> None:
        self.query_one("#status", Static).update(message.status_text)


def run() -> None:
    MinesweeperApp().run()


if __name__ == "__main__":
    run()
