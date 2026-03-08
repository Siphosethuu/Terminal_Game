import curses
from math import ceil
from typing import List
from tetris.shapes import Shape
from random import  randint
from consts import hide_cursor


class Game:
    def __init__(self) -> None:
        self.screen: curses.window = curses.newwin(
            curses.LINES, curses.COLS, 0, 0
        )

        self.score: int = 0
        self.screen.nodelay(True)
        self.screen.keypad(True)

    @hide_cursor()
    def start(self) -> None:
        Shape.set_screen(self.screen)
        shape: Shape = self.generate_shape()
        grounded: List[Shape] = []
        value: float = 0.0
        while True:
            self.screen.clear()
            shape.display()
            value += 0.00000001
            if ceil(value) == 1:
                shape.fall()
                self.screen.addstr(0, 0, f"Down. ({shape.y})")
                value = 0.0
            self.screen.refresh()
            if shape.is_grounded:
                grounded.append(shape)
                shape = self.generate_shape()

            key: int = self.screen.getch()
            match key:
                case 27:
                    exit()
                case _:
                    pass

    def generate_shape(self) -> Shape:
        return Shape('L')


