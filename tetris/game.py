import curses
from math import ceil
from typing import List, Tuple
from tetris.shapes import Shape
from random import  choice
from consts import Keys, BLOCK, hide_cursor

shapes: List[str] = ['L', 'J', 'Z', 'S', 'T', 'O']
class Game:
    def __init__(self, stdscr: curses.window) -> None:
        self.screen: curses.window = curses.newwin(
            curses.LINES, curses.COLS, 0, 0
        )
        self.bg_window = stdscr

        self.score: int = 0
        self.screen.nodelay(True)
        self.screen.keypad(True)

    @hide_cursor() # type: ignore
    def start(self) -> None:
        shape: Shape = self.generate_shape()
        grounded: List[Tuple] = []
        while True:
            self.screen.clear()
            shape.display(self.screen)
            curses.napms(64)
            shape.fall(self.screen)
            curses.napms(64)
            # shape.rotate(self.screen)
            for y, x, char in grounded:
                self.screen.addstr(y, x, char)
            self.screen.refresh()
            if shape.is_grounded:

                for y, x in shape.body:
                    new_y, new_x = shape.y+y,shape.x+x
                    grounded.append(
                        (new_y, new_x, BLOCK)
                    )
                shape = self.generate_shape()
            key: int = self.screen.getch()
            match key:
                case Keys.ESC:
                    exit()
                case "KEY_LEFT"
                case _:
                    pass

    def generate_shape(self) -> Shape:
        return Shape(choice(shapes))


