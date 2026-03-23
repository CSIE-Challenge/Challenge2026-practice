from __future__ import annotations

from dataclasses import dataclass

from minesweeper.utils.helpers import count_adjacent_mines

import random


@dataclass(slots=True)
class Cell:
    x: int
    y: int
    has_mine: bool = False
    revealed: bool = False
    flagged: bool = False
    adjacent_mines: int = 0


def create_board(
    width: int, height: int, mine_count: int, first_reveal: tuple[int, int]
) -> list[list[Cell]]:

    all_possible_mine_positions = [
        (x, y) for x in range(width) for y in range(height) if (x, y) != first_reveal
    ]
    mine_positions = random.sample(all_possible_mine_positions, k=mine_count)

    board = [
        [Cell(x=x, y=y, has_mine=(x, y) in mine_positions) for x in range(width)]
        for y in range(height)
    ]

    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            cell.adjacent_mines = count_adjacent_mines(board, x, y)

    return board
