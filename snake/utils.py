import curses

from typing import Dict
from consts import LINES, COLS
from enum import Enum
from snake.stage import Stage
    
BODY_PART: str = '  '
SNAKE_FOOD: str = ' ©'


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



class Keys:
    UP: int = curses.KEY_UP
    ESC: int = 27
    DOWN: int = curses.KEY_DOWN
    LEFT: int = curses.KEY_LEFT
    RIGHT: int = curses.KEY_RIGHT



def get_box_stage() -> Stage:
    INFO = {}
    for y in range(1, LINES):
        INFO[(y, 0)] = ' '
        INFO[(y, 1)] = ' '
        INFO[(y, COLS - 1)] = ' '
        INFO[(y, COLS - 2)] = ' '
        INFO[(y, COLS - 3)] = ''


    for x in range(0, COLS + 1):
        INFO[(1, x)] = ' '
        INFO[(LINES, x)] = ' '

    return Stage(INFO)


