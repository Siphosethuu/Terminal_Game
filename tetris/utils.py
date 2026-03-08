


from typing import Dict, List, Tuple
from consts import COLS, LINES, Direction

WIDTH: int = 20
HEIGHT: int = 40


x: int = ( COLS - WIDTH ) // 2
y: int = (LINES - HEIGHT ) // 2
SHAPES: Dict[str, List[set[Tuple[int, int]]]] = {
    'L': [
        {(0, 0), (0, 1), (-1, 1), (0, -1)},
        {(0, 0), (1, 0), (-1, 0), (1, 1)},
        {(0, 0), (0, -1), (0, 1), (1, -1)},
        {(0, 0), (-1, 0), (-1, -1), (1, 0)}],
    'O': [
        {(0, 0), (0, 1), (1, 0), (1, 1)}
        ]
}

ROTATION_DIRS: List[Direction] = [
    Direction.NONE, Direction.RIGHT, Direction.LEFT]

TOP_LEFT_CORNER: Tuple[int, int] = (0, 0)
BOTTOM_RIGHT_CORNER: Tuple[int, int] = (LINES, COLS)


