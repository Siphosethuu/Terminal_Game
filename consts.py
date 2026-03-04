


from os import get_terminal_size
from typing import Dict 
from enum import Enum

SIZE = get_terminal_size()

COLS: int = SIZE.columns
LINES: int = SIZE.lines

BLOCK: str = "  "



class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -2)
    RIGHT = (0, 2)

    def __init__(self, y: int, x: int) -> None:
        self.y = y
        self.x = x

    @property
    def opposite(self) -> "Direction":

        opposites: Dict[str, Direction] = {
            "UP": Direction.DOWN, 
            "DOWN": Direction.UP,
            "LEFT": Direction.RIGHT,
            "RIGHT": Direction.LEFT 
        }

        return opposites[self.name]

