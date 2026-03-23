from textual.app import App, ComposeResult
from textual.containers import Container, Vertical
from textual.widgets import Static

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
        width: auto;
        height: auto;
        padding: 1;
    }

    #chrome {
        width: auto;
        max-width: 62;
        height: auto;
        margin: 0;
    }

    #workspace {
        width: auto;
        height: auto;
    }

    .panel {
        border: round $panel;
        background: $surface;
        padding: 1;
    }

    #board-panel {
        width: auto;
    }

    .panel-title {
        color: $primary;
        text-style: bold;
        padding: 0 0 1 0;
    }

    #status {
        border: round $secondary;
        background: $panel;
        color: $foreground;
        padding: 1 1;
        margin-bottom: 1;
    }

    #howto {
        color: #e5e9f0;
        padding-bottom: 1;
    }

    #legend {
        color: #d8dee9;
        padding-top: 1;
    }

    #game-note {
        color: #a7b4c8;
        padding-top: 1;
    }
    """

    def __init__(self) -> None:
        super().__init__()
        self.theme = "nord"
        self.game_state = GameState()
        self._last_game_over_message: str | None = None

    def compose(self) -> ComposeResult:
        with Container(id="app-shell"):
            with Vertical(id="chrome"):
                with Vertical(id="workspace"):
                    with Vertical(id="board-panel", classes="panel"):
                        yield Static("Minesweeper", classes="panel-title")
                        yield Static(self.game_state.status_text, id="status")
                        yield Static(
                            "Click: reveal  •  Right Click: flag  •  Shift + Click: fallback flag",
                            id="howto",
                        )
                        yield BoardView(self.game_state)
                        yield Static(
                            "Legend: blank = hidden or empty, F = flag, 1-8 = adjacent mines, * = mine",
                            id="legend",
                        )
                        yield Static(
                            "Reveal every safe cell and avoid mines.",
                            id="game-note",
                        )

    def on_board_view_changed(self, message: BoardView.Changed) -> None:
        status = self.query_one("#status", Static)
        is_win = self.game_state.game_over and self.game_state.is_win()
        is_lose = self.game_state.game_over and self.game_state.is_lose()
        if self.game_state.game_over:
            status.update("Game finished. Restart the app to play again.")
        else:
            status.update(message.status_text)

        if (
            self.game_state.game_over
            and message.status_text != self._last_game_over_message
        ):
            severity = "information" if is_win else "error"
            self.notify(message.status_text, title="Game Result", severity=severity)
            self._last_game_over_message = message.status_text


def run() -> None:
    MinesweeperApp().run()


if __name__ == "__main__":
    run()
