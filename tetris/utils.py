import curses


from typing import Dict, List, Tuple
from consts import COLS, LINES, Direction

WIDTH: int = 20
HEIGHT: int = 40


x: int = ( COLS - WIDTH ) // 2
y: int = (LINES - HEIGHT ) // 2
SHAPES = {
    'L': { 
        "COLOR": 2,
        "ROTATIONS": [
            {(0, 0), (0, 2), (-1, 2), (0, -2)},
            {(0, 0), (1, 0), (-1, 0), (1, 2)},
            {(0, 0), (0, -2), (0, 2), (1, -2)},
            {(0, 0), (-1, 0), (-1, -2), (1, 0)}
        ]
    },
    'J': {
        "COLOR": 3,
        "ROTATIONS": [
            {(0, 0), (0, -2), (-1, -2), (0, 2)},
            {(1, 0), (0, 0), (-1, 0), (-1, 2)},
            {(0, -2), (0, 0), (0, 2), (1, 2)},
            {(-1, 0), (0, 0), (1, 0), (1, -2)} 
        ]
    },
    'S': {
        "COLOR": 4,
        "ROTATIONS": [
            {(-1, -2), (-1, 0), (0, 0), (0, 2)},
            {(0, 0), (0, 2), (-1, 2), (1, 0)},
            {(0, 0), (0, -2), (1, 0), (1, 2)},
            {(0, 0), (0, -2), (1, -2), (-1, 0)}
        ]
    },
    'Z': {
        "COLOR": 5,
        "ROTATIONS": [
            {(-1, 2), (-1, 0), (0, 0), (0, -2)},
            {(0, 0), (0, -2), (-1, -2), (1, 0)},
            {(0, 0), (0, 2), (1, 0), (1, -2)},
            {(0, 0), (0, 2), (1, 2), (-1, 0)}
        ]
    },
    'T':  {
        "COLOR": 6,
        "ROTATIONS": [
            {(-1, 0), (0, 0), (0, 2), (0, -2)},
            {(0, 0), (0, 2), (-1, 0), (1, 0)},
            {(0, 0), (0, 2), (1, 0), (0, -2)},
            {(0, 0), (0, -2), (1, 0), (-1, 0)}
        ]
    },
    'O': {
        "COLOR": 7,
        "ROTATIONS": [
        {(0, 0), (0, 2), (1, 0), (1, 2)}
        ]
    }
}

ROTATION_DIRS: List[Direction] = [
    Direction.NONE, Direction.RIGHT, Direction.LEFT]

TOP_LEFT_CORNER: Tuple[int, int] = (0, 0)
BOTTOM_RIGHT_CORNER: Tuple[int, int] = (LINES, COLS)


