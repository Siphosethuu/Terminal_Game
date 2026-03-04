import curses
from typing import List
from tetris.shapes import Shape



class Game:
    def __init__(self) -> None:
        self.screen: curses.window = curses.newwin(
            curses.LINES, curses.COLS, 0, 0
        )

        self.score: int = 0
        self.screen.nodelay(True)
        self.screen.keypad(True)

    def start(self) -> None:
        shape: Shape = self.generate_shape()
        grounded: List[Shape] = []
        while True:
            shape.display(self.screen)
            shape.fall(self.screen)
            for b in grounded:
                b.display(self.screen)
            if shape.is_down:
                grounded.append(shape)
                shape = self.generate_shape()

            key: int = self.screen.getch()
            curses.napms(64)
            match key:
                case 27:
                    exit()
                case _:
                    pass

    def generate_shape(self) -> Shape:
        return Shape((0, 10), (0, 0), (0,1), (1, 0), (1, 1), color=curses.A_STANDOUT)


