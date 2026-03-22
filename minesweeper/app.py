from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Footer, Header, Static

from minesweeper.game.state import GameState
from minesweeper.ui.board_view import BoardView


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

    #status {
        padding-bottom: 1;
    }
    """

    def __init__(self) -> None:
        super().__init__()
        self.game_state = GameState()

    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id="app-shell"):
            yield Static(self.game_state.status_text, id="status")
            yield BoardView(self.game_state)
        yield Footer()

    def on_board_view_changed(self, message: BoardView.Changed) -> None:
        self.query_one("#status", Static).update(message.status_text)


def run() -> None:
    MinesweeperApp().run()


if __name__ == "__main__":
    run()
