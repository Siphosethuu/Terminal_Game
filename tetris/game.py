import curses
from math import ceil
from typing import List, Tuple
from tetris.shape import Shape
from random import  choice, shuffle
from consts import BLOCK, hide_cursor
from threading import Lock, Thread

shapes: List[str] = ['L', 'J', 'Z', 'S', 'T', 'O']
class Game:
    def __init__(self, screen: curses.window) -> None:
        self.screen = screen
        self.shapes: List[Shape] = Shape.create_shapes(self.screen)
        self.lock: Lock = Lock()
        self.score: int = 0
        self.screen.nodelay(True)
        self.screen.keypad(True)

    @hide_cursor() # type: ignore
    def start(self) -> None:
        shuffle(self.shapes)
        shape: Shape = self.shapes.pop()
        while self.shapes:
            shape.fall()
            curses.napms(64)
            if shape.is_grounded:
                shape = self.shapes.pop()
            shape.input()
            shape.rotate()
            curses.napms(250)

            



