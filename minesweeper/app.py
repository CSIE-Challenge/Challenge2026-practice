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
        background: #0b1220;
        color: #f5f7ff;
    }

    #app-shell {
        width: 1fr;
        height: 1fr;
        padding: 1 2;
    }

    #chrome {
        width: 1fr;
        max-width: 110;
        height: auto;
        margin: 1 0;
    }

    #hero {
        width: 1fr;
        padding: 1 2 0 2;
        color: #f8fafc;
        text-style: bold;
    }

    #subtitle {
        width: 1fr;
        padding: 0 2 1 2;
        color: #9fb0c9;
    }

    #workspace {
        width: 1fr;
        height: auto;
    }

    .panel {
        border: round #31405f;
        background: #111a2c;
        padding: 1 2;
    }

    #board-panel {
        width: auto;
        margin-right: 1;
    }

    #side-panel {
        width: 28;
        min-width: 28;
    }

    .panel-title {
        color: #7dd3fc;
        text-style: bold;
        padding-bottom: 1;
    }

    #status {
        border: round #35507a;
        background: #16233c;
        color: #eff6ff;
        padding: 1 1;
        margin-bottom: 1;
    }

    #tips {
        color: #bfd0ea;
        margin-bottom: 1;
    }

    #legend {
        color: #d5e1f5;
    }
    """

    def __init__(self) -> None:
        super().__init__()
        self.game_state = GameState()

    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id="app-shell"):
            with Vertical(id="chrome"):
                yield Static("Minesweeper Starter", id="hero")
                yield Static(
                    "A small Textual project for practicing branches, pull requests, and merge conflicts.",
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
                            "Left click reveals one cell.\n"
                            "Some features are intentionally incomplete so the repo can be used for collaboration practice.",
                            id="tips",
                        )
                        yield Static(
                            "Legend\n"
                            "[ ] Hidden cell\n"
                            "[1-8] Adjacent mines\n"
                            "[*] Mine after reveal",
                            id="legend",
                        )
        yield Footer()

    def on_board_view_changed(self, message: BoardView.Changed) -> None:
        self.query_one("#status", Static).update(message.status_text)


def run() -> None:
    MinesweeperApp().run()


if __name__ == "__main__":
    run()
