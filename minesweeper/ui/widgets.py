from __future__ import annotations

from textual.widgets import Button
from textual.messages import Message
from textual import events

from minesweeper.game.board import Cell


class CellButton(Button):
    def __init__(self, x: int, y: int, cell: Cell) -> None:
        super().__init__(self._label_for(cell), id=f"cell-{x}-{y}")
        self.x = x
        self.y = y
        self.can_focus = False
        self.flat = True
        self.sync_with_cell(cell)

    class ClickedAction(Message):
        def __init__(self, button: "CellButton", is_flag_action: bool) -> None:
            self.button = button
            self.is_flag_action = is_flag_action
            super().__init__()

    @staticmethod
    def _label_for(cell: Cell) -> str:
        if not cell.revealed:
            if cell.flagged:
                return "F"
            return " "

        if cell.has_mine:
            return "*"

        if cell.adjacent_mines == 0:
            return " "

        return str(cell.adjacent_mines)

    def sync_with_cell(self, cell: Cell) -> None:
        self.label = self._label_for(cell)
        self.set_class(not cell.revealed, "-hidden")
        self.set_class(cell.revealed, "-revealed")
        self.set_class(cell.flagged and not cell.revealed, "-flagged")
        self.set_class(
            cell.revealed and cell.adjacent_mines == 0 and not cell.has_mine, "-empty"
        )
        self.set_class(cell.revealed and cell.has_mine, "-mine")

        for count in range(1, 9):
            self.set_class(
                cell.revealed and not cell.has_mine and cell.adjacent_mines == count,
                f"-count-{count}",
            )

    def on_click(self, event: events.Click) -> None:
        event.stop()
        is_flag_action = event.button == 3 or event.shift
        self.post_message(self.ClickedAction(self, is_flag_action))
