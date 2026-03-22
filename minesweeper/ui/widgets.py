from __future__ import annotations

from textual.widgets import Button

from minesweeper.game.board import Cell


class CellButton(Button):
    def __init__(self, x: int, y: int, cell: Cell) -> None:
        super().__init__(self._label_for(cell), id=f"cell-{x}-{y}")
        self.x = x
        self.y = y
        self.can_focus = False

    @staticmethod
    def _label_for(cell: Cell) -> str:
        if not cell.revealed:
            return "[]"

        if cell.has_mine:
            return "*"

        if cell.adjacent_mines == 0:
            return "."

        return str(cell.adjacent_mines)

    def sync_with_cell(self, cell: Cell) -> None:
        self.label = self._label_for(cell)

    # TODO: Support right-click flag / unflag here and update the widget label or
    # style to reflect flagged cells. The starter only wires left-click reveal so
    # this can be owned as a separate collaboration issue.
