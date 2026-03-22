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
        background: #0f172a;
        padding: 1;
        border: round #23314d;
    }

    BoardView Grid {
        grid-size: 8 8;
        grid-columns: 5 5 5 5 5 5 5 5;
        grid-rows: 3 3 3 3 3 3 3 3;
        grid-gutter: 1 1;
    }

    BoardView CellButton {
        min-width: 5;
        height: 3;
        content-align: center middle;
        border: round #334155;
        background: #1e293b;
        color: #e2e8f0;
        text-style: bold;
    }

    BoardView CellButton.-hidden {
        background: #334155;
        color: #cbd5e1;
        border: round #475569;
    }

    BoardView CellButton.-revealed {
        background: #e2e8f0;
        color: #0f172a;
        border: round #94a3b8;
    }

    BoardView CellButton.-empty {
        color: #94a3b8;
    }

    BoardView CellButton.-mine {
        background: #b91c1c;
        color: #fff7ed;
        border: round #ef4444;
    }

    BoardView CellButton.-count-1 {
        color: #2563eb;
    }

    BoardView CellButton.-count-2 {
        color: #15803d;
    }

    BoardView CellButton.-count-3 {
        color: #dc2626;
    }

    BoardView CellButton.-count-4 {
        color: #7c3aed;
    }

    BoardView CellButton.-count-5 {
        color: #c2410c;
    }

    BoardView CellButton.-count-6 {
        color: #0f766e;
    }

    BoardView CellButton.-count-7 {
        color: #be123c;
    }

    BoardView CellButton.-count-8 {
        color: #1f2937;
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
