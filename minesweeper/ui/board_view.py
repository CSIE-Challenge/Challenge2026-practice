from __future__ import annotations

from textual.app import ComposeResult
from textual.containers import Grid
from textual.message import Message
from textual.widget import Widget
from textual.widgets import Label

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
        background: transparent;
        padding: 0;
        border: none;
    }

    BoardView Grid {
        grid-size: 11 11;
        grid-columns: 5 5 5 5 5 5 5 5 5;
        grid-rows: 3 3 3 3 3 3 3 3 3;
        grid-gutter: 0 0;
    }

    BoardView CellButton {
        min-width: 5;
        height: 3;
        content-align: center middle;
        border: round $panel;
        background: $panel;
        color: $foreground;
        text-style: bold;
    }

    BoardView CellButton.-hidden {
        background: #434c5e;
        color: #d8dee9;
        border: round #4c566a;
    }

    BoardView CellButton.-revealed {
        background: #00ff00;
        color: #2e3440;
        border: round #d8dee9;
    }

    BoardView CellButton.-flagged {
        background: #1f1e33;
        color: #008000;
        border: round #d8dee9;
    }

    BoardView CellButton.-empty {
        color: #ff0000;
    }

    BoardView CellButton.-mine {
        background: #bf616a;
        color: #eceff4;
        border: round #d08770;
    }

    BoardView CellButton.-count-1 {
        color: #5e81ac;
    }

    BoardView CellButton.-count-2 {
        color: #a3be8c;
    }

    BoardView CellButton.-count-3 {
        color: #bf616a;
    }

    BoardView CellButton.-count-4 {
        color: #b48ead;
    }

    BoardView CellButton.-count-5 {
        color: #d08770;
    }

    BoardView CellButton.-count-6 {
        color: #88c0d0;
    }

    BoardView CellButton.-count-7 {
        color: #8fbcbb;
    }

    BoardView CellButton.-count-8 {
        color: #4c566a;
    }

    BoardView .coord-label {
        width: 5;
        height: 3;
        content-align: center middle;
        background: transparent;
        color: $foreground;
        text-style: bold;
    }
    """

    def __init__(self, state: GameState) -> None:
        super().__init__()
        self.state = state

    def compose(self) -> ComposeResult:
        with Grid():
            yield Label(str(""), classes="coord-label")
            for x in range(self.state.width):
                yield Label(str(x), classes="coord-label")
            for y, row in enumerate(self.state.board):
                yield Label(str(y), classes="coord-label")
                for x, cell in enumerate(row):
                    yield CellButton(x, y, cell)

    # def on_button_pressed(self, event: CellButton.Pressed) -> None:
    #     cell_button = event.button
    #     if event.shift:
    #         self.state.toggle_flag(cell_button.x, cell_button.y)
    #     else:
    #         self.state.reveal_cell(cell_button.x, cell_button.y)
    #     self.refresh_board()
    #     self.post_message(self.Changed(self.state.status_text))

    def on_cell_button_clicked_action(self, event: CellButton.ClickedAction) -> None:
        cell_button = event.button

        # 完美的互斥邏輯：有 Shift 就插旗，沒有就翻開
        if event.shift:
            # print("meow")
            # self.state.reveal_cell(cell_button.x, cell_button.y)
            self.state.toggle_flag(cell_button.x, cell_button.y)
        else:
            # print("qq")
            self.state.reveal_cell(cell_button.x, cell_button.y)

        self.refresh_board()
        self.post_message(self.Changed(self.state.status_text))

    def refresh_board(self) -> None:
        for button in self.query(CellButton):
            button.sync_with_cell(self.state.cell_at(button.x, button.y))

    # TODO: Add visible row / column coordinates here and tighten the board layout
    # so positions are easier to read at a glance.
