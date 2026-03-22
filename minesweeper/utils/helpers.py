from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from minesweeper.game.board import Cell


def iter_neighbor_positions(
    board: list[list[Cell]], x: int, y: int
) -> list[tuple[int, int]]:
    positions: list[tuple[int, int]] = []

    if not board:
        return positions

    height = len(board)
    width = len(board[0])

    for y_offset in (-1, 0, 1):
        for x_offset in (-1, 0, 1):
            if x_offset == 0 and y_offset == 0:
                continue

            next_x = x + x_offset
            next_y = y + y_offset

            if 0 <= next_x < width and 0 <= next_y < height:
                positions.append((next_x, next_y))

    return positions


def count_adjacent_mines(board: list[list[Cell]], x: int, y: int) -> int:
    return sum(1 for nx, ny in iter_neighbor_positions(board, x, y) if board[ny][nx].has_mine)
