import curses

from os import get_terminal_size
from typing import Dict, Tuple 
from enum import Enum
from curses import A_ATTRIBUTES, A_CHARTEXT, curs_set, window
SIZE = get_terminal_size()

COLS: int = SIZE.columns
LINES: int = SIZE.lines

BLOCK: str = '⬛'


class Keys:
    UP: int = curses.KEY_UP
    ESC: int = 27
    DOWN: int = curses.KEY_DOWN
    LEFT: int = curses.KEY_LEFT
    RIGHT: int = curses.KEY_RIGHT


class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -2)
    NONE = (0, 0)
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

import functools

def hide_cursor(func):
    @functools.wraps(func) 
    def wrapper(*args, **kwargs):
        OLD_CURS: int = curs_set(0)
        try:
            func(*args, **kwargs) # type: ignore
        finally:
            curs_set(OLD_CURS)
    return wrapper

def draw_square_boundary(screen: window, *args: int, char: str = "  ") -> None:
    if len(args) != 4:
        raise ValueError("Invalid args: {args}. Should be, start_y, start_x, end_y, end_x.")


    start_y, start_x, end_y, end_x = args
    left = start_x - 2
    top = start_y - 1
    for y in range(start_y , end_y):
        screen.addstr(y, left, char, curses.A_STANDOUT)
        screen.addstr(y, end_x, char, curses.A_STANDOUT)

    for x in range(left, end_x + 2, 2):
        screen.addstr(top, x, char, curses.A_STANDOUT)
        screen.addstr(end_y, x, char, curses.A_STANDOUT)


def clear(screen: window, start_y: int, start_x: int, end_y: int, end_x: int) -> None:
    bkgd_char: str = chr(screen.getbkgd() & A_CHARTEXT)
    bkgd_attr: int = screen.getbkgd() & A_ATTRIBUTES
    for y in range(start_y, end_y):
        for x in range(start_x, end_x):
            screen.addstr(y, x, bkgd_char, bkgd_attr)
