import curses

from typing import Tuple



class SnakeDirection:
    UP: Tuple[int, int] = (-1, 0)
    DOWN: Tuple[int, int] = (1, 0)
    LEFT: Tuple[int, int] = (0, -1)
    RIGHT: Tuple[int, int] = (0, 1)

class Keys:
    UP: int = curses.KEY_UP
    ESC: int = 27
    DOWN: int = curses.KEY_DOWN
    LEFT: int = curses.KEY_LEFT
    RIGHT: int = curses.KEY_RIGHT

