import curses

from typing import Dict, Tuple
from enum import Enum
from consts import LINES, COLS


class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT  = (0, -1)
    RIGHT = (0, 1)

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



class Keys:
    UP: int = curses.KEY_UP
    ESC: int = 27
    DOWN: int = curses.KEY_DOWN
    LEFT: int = curses.KEY_LEFT
    RIGHT: int = curses.KEY_RIGHT


def get_box_stage() -> Dict[Tuple[int, int], int]:
    global LINES, COLS

    stage = {}

    for y in range(1, LINES - 1):

        stage[(y, 0)] = 0
        stage[(y, COLS - 3)] = 0

    for x in range(0, COLS - 1):
        stage[(1, x)] = 0
        stage[(LINES - 3, x)] = 0

    return stage

def get_tunnel_stage() -> Dict[Tuple[int, int], int]:

    stage = {}

    return stage


SNAKE_FOOD: str = ' ©'
BODY_PART : str = '  '
