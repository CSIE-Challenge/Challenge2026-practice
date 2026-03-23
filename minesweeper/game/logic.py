from __future__ import annotations

from minesweeper.game.board import Cell


def reveal_cells(board: list[list[Cell]], x: int, y: int) -> list[Cell]:
    if not within_bounds(board, x, y):
        return []

    cell = board[y][x]
    if cell.revealed or cell.flagged:
        return []

    cell.revealed = True
    revealed_cells = [cell]
    print("PixelCat <3")

    # TODO: Implement flood fill so revealing an empty cell also reveals nearby
    # empty neighbors and their borders. Right now the starter only reveals one
    # cell at a time to leave a focused issue for students.
    return revealed_cells


def within_bounds(board: list[list[Cell]], x: int, y: int) -> bool:
    if not board:
        return False

    return 0 <= y < len(board) and 0 <= x < len(board[0])
