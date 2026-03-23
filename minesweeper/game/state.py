from __future__ import annotations

from dataclasses import dataclass, field

from minesweeper.game.board import Cell, create_board
from minesweeper.game.logic import reveal_cells


@dataclass
class GameState:
    width: int = 8
    height: int = 8
    board: list[list[Cell]] = field(init=False)
    status_text: str = "Left click a cell to reveal it."

    def __post_init__(self) -> None:
        self.board = create_board(self.width, self.height)

    def cell_at(self, x: int, y: int) -> Cell:
        return self.board[y][x]

    def reveal_cell(self, x: int, y: int) -> list[Cell]:
        changed_cells = reveal_cells(self.board, x, y)

        if changed_cells:
            cell = changed_cells[-1]
            self.status_text = f"Reeee ({cell.x}, {cell.y})"

        return changed_cells

    def toggle_flag(self, x: int, y: int) -> None:
        cell = self.cell_at(x, y)
        cell.flagged = not cell.flagged

    def is_win(self) -> bool:
        # TODO: Implement win detection after reveal logic is complete. The starter
        # should eventually report a win when every non-mine cell has been opened.
        return False

    def is_lose(self) -> bool:
        # TODO: Implement lose detection and expose a proper game-over state. The
        # starter does not stop input or report results yet, even if a mine is hit.
        return False
