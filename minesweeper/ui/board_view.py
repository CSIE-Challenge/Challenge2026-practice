from __future__ import annotations

from textual.app import ComposeResult
from textual.containers import Grid
from textual.message import Message
from textual.widget import Widget

from minesweeper.game.state import GameState
from minesweeper.ui.widgets import CellButton


class BoardView(Widget):
    class Changed(Message):
        def __init__(self, status_text: str) -> None:
            self.status_text = status_text
            super().__init__()

    DEFAULT_CSS = """
    BoardView {
        width: auto;
        height: auto;
    }

    BoardView Grid {
        grid-size: 8 8;
        grid-columns: 4 4 4 4 4 4 4 4;
        grid-rows: 3 3 3 3 3 3 3 3;
        gutter: 0;
    }

    BoardView CellButton {
        min-width: 4;
        height: 3;
    }
    """

    def __init__(self, state: GameState) -> None:
        super().__init__()
        self.state = state

    def compose(self) -> ComposeResult:
        with Grid():
            for y, row in enumerate(self.state.board):
                for x, cell in enumerate(row):
                    yield CellButton(x, y, cell)

    def on_button_pressed(self, event: CellButton.Pressed) -> None:
        cell_button = event.button
        self.state.reveal_cell(cell_button.x, cell_button.y)
        self.refresh_board()
        self.post_message(self.Changed(self.state.status_text))

    def refresh_board(self) -> None:
        for button in self.query(CellButton):
            button.sync_with_cell(self.state.cell_at(button.x, button.y))

    # TODO: Improve board rendering here. Add visible coordinates, clearer spacing,
    # and a more readable color/styling scheme so the grid is easier to understand.
