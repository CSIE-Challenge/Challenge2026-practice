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

    # TODO: Implement flood fill so revealing an empty cell also reveals nearby
    # empty neighbors and their borders. Right now the starter only reveals one
    # cell at a time to leave a focused issue for students.
    if cell.adjacent_mines > 0:
        return revealed_cells

    for i in [0, 1, -1]:
        for j in [0, 1, -1]:
            if i == 0 and j == 0:
                continue

            new_x = x + i
            new_y = y + j

            if within_bounds(board, new_x, new_y):
                new_cell = board[new_y][new_x]
                if new_cell.has_mine:
                    continue

                revealed_cells.extend(reveal_cells(board, new_x, new_y))

    return revealed_cells


def within_bounds(board: list[list[Cell]], x: int, y: int) -> bool:
    if not board:
        return False

    return 0 <= y < len(board) and 0 <= x < len(board[0])
