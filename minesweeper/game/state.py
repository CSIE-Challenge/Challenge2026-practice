from __future__ import annotations

from dataclasses import dataclass, field

from minesweeper.game.board import Cell, create_board
from minesweeper.game.logic import reveal_cells


@dataclass
class GameState:
    width: int = 8
    height: int = 8
    mine_count: int = 6
    board: list[list[Cell]] = field(init=False)
    status_text: str = "Click to reveal. Right click or Shift + Click to flag."
    is_first_reveal: bool = True
    game_over: bool = False

    def __post_init__(self) -> None:
        self.board = [
            [Cell(x=x, y=y, has_mine=False) for x in range(self.width)]
            for y in range(self.height)
        ]

    def cell_at(self, x: int, y: int) -> Cell:
        return self.board[y][x]

    def reveal_cell(self, x: int, y: int) -> list[Cell]:
        if self.game_over:
            return []

        if self.is_first_reveal:
            flagged_positions = {
                (cell.x, cell.y)
                for row in self.board
                for cell in row
                if cell.flagged and (cell.x, cell.y) != (x, y)
            }
            self.board = create_board(self.width, self.height, self.mine_count, (x, y))
            for flagged_x, flagged_y in flagged_positions:
                self.board[flagged_y][flagged_x].flagged = True
            self.is_first_reveal = False

        changed_cells = reveal_cells(self.board, x, y)

        if changed_cells:
            cell = changed_cells[-1]
            self.status_text = f"Revealed ({cell.x}, {cell.y})"
        if self.is_win():
            self.game_over = True
            self.status_text = "You win! All safe cells are revealed."
        if self.is_lose():
            self.game_over = True
            self.status_text = "You hit a mine. Game over."

        return changed_cells

    def toggle_flag(self, x: int, y: int) -> None:
        if self.game_over:
            return

        cell = self.cell_at(x, y)
        if not cell.revealed:
            cell.flagged = not cell.flagged
            if cell.flagged:
                self.status_text = f"Flagged ({x}, {y})"
            else:
                self.status_text = f"Removed flag from ({x}, {y})"

    def is_win(self) -> bool:
        for row in self.board:
            for cell in row:
                if cell.has_mine is False and cell.revealed is False:
                    return False
        return True

    def is_lose(self) -> bool:
        for row in self.board:
            for cell in row:
                if cell.has_mine is True and cell.revealed is True:
                    return True
        return False
