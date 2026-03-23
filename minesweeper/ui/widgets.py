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
        self.sync_with_cell(cell)

    class ClickedAction(Message):
        def __init__(self, button: "CellButton", shift: bool) -> None:
            self.button = button
            self.shift = shift
            super().__init__()

    @staticmethod
    def _label_for(cell: Cell) -> str:
        if not cell.revealed:
            if cell.flagged:
                return "*"
            return " "

        if cell.has_mine:
            return "*"

        if cell.adjacent_mines == 0:
            return " "

        if cell.adjacent_mines == 100:
            return "?"

        return str(cell.adjacent_mines)

    def sync_with_cell(self, cell: Cell) -> None:
        self.label = self._label_for(cell)
        self.set_class(not cell.revealed, "-hidden")
        self.set_class(cell.revealed, "-revealed")
        self.set_class(cell.flagged, "-flagged")
        self.set_class(
            cell.revealed and cell.adjacent_mines == 0 and not cell.has_mine, "-empty"
        )
        self.set_class(cell.revealed and cell.has_mine, "-mine")

        for count in range(1, 9):
            self.set_class(
                cell.revealed and not cell.has_mine and cell.adjacent_mines == count,
                f"-count-{count}",
            )

    # TODO: Support right-click flag / unflag here and update the widget label or
    # style to reflect flagged cells. The starter only wires left-click reveal so
    # this can be owned as a separate collaboration issue.

    def on_click(self, event: events.Click) -> None:
        event.stop()  # 阻擋預設不帶 shift 的 Pressed 事件
        self.post_message(self.ClickedAction(self, event.shift))
