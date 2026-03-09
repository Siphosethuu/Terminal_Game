import curses


from typing import Dict, List, Tuple
from consts import COLS, LINES, Direction

WIDTH: int = 20
HEIGHT: int = 40


x: int = ( COLS - WIDTH ) // 2
y: int = (LINES - HEIGHT ) // 2
SHAPES: Dict[str, List[set[Tuple[int, int]]]] = {
    'L': [
        {(0, 0), (0, 2), (-1, 2), (0, -2)},
        {(0, 0), (1, 0), (-1, 0), (1, 2)},
        {(0, 0), (0, -2), (0, 2), (1, -2)},
        {(0, 0), (-1, 0), (-1, -2), (1, 0)}],
    'J': [
        {(0, 0), (0, -2), (-1, -2), (0, 2)},
        {(1, 0), (0, 0), (-1, 0), (-1, 2)},
        {(0, -2), (0, 0), (0, 2), (1, 2)},
        {(-1, 0), (0, 0), (1, 0), (1, -2)}
        ],
    'S': [
        {(-1, -2), (-1, 0), (0, 0), (0, 2)},
        {(0, 0), (0, 2), (-1, 2), (1, 0)},
        {(0, 0), (0, -2), (1, 0), (1, 2)},
        {(0, 0), (0, -2), (1, -2), (-1, 0)}
        ],
    'Z': [
        {(-1, 2), (-1, 0), (0, 0), (0, -2)},
        {(0, 0), (0, -2), (-1, -2), (1, 0)},
        {(0, 0), (0, 2), (1, 0), (1, -2)},
        {(0, 0), (0, 2), (1, 2), (-1, 0)}
        ],
    'T':  [
        {(-1, 0), (0, 0), (0, 2), (0, -2)},
        {(0, 0), (0, 2), (-1, 0), (1, 0)},
        {(0, 0), (0, 2), (1, 0), (0, -2)},
        {(0, 0), (0, -2), (1, 0), (-1, 0)}
        ],
    'O': [
        {(0, 0), (0, 2), (1, 0), (1, 2)}
        ]
}
COLORS: Dict[str, int] = {
    'L': curses.COLOR_BLUE,
    'J': curses.COLOR_WHITE,
    'S': curses.COLOR_RED,
    'Z': curses.COLOR_GREEN,
    'T': curses.COLOR_MAGENTA,
    'O': curses.COLOR_YELLOW

    }

ROTATION_DIRS: List[Direction] = [
    Direction.NONE, Direction.RIGHT, Direction.LEFT]

TOP_LEFT_CORNER: Tuple[int, int] = (0, 0)
BOTTOM_RIGHT_CORNER: Tuple[int, int] = (LINES, COLS)


