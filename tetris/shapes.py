


from itertools import cycle
from typing import Tuple
from consts import Direction, BLOCK
from curses import A_CHARTEXT, window
from tetris.utils import TOP_LEFT_CORNER, BOTTOM_RIGHT_CORNER


OPERATIONS: cycle = cycle([
    lambda pos: (pos[1], pos[0]), lambda pos: (-pos[1], -pos[0])
    ]
)


class Shape:

    def __init__(self, *args: Tuple[int, int], color: int) -> None:
        self.y, self.x = args[0]
        self.body = [pos for pos in args[1:]]
        self.color = color
        self.is_down: bool = False

    def rotate_shape(self) -> None:
        # rotate: "function" = next(OPERATIONS)
        raise NotImplementedError


    def fall(self, screen: window) -> None:
        floor, _ = BOTTOM_RIGHT_CORNER
        self.y += 1
        y, x = max(self.body, key=lambda pos: pos[0])
        pos: int = self.y + 1
        if pos == floor:
            self.is_down = True
        char = chr(screen.inch(pos, self.x + x) & A_CHARTEXT)
        if char == ' ':
            self.is_down = True
            return
            


    def translate(self, direction: Direction) -> None:
        match direction:
            case Direction.RIGHT:
                _, max_value = max(self.body, key=lambda pos: pos[1])
                _, limit = BOTTOM_RIGHT_CORNER
                if self.x + max_value < limit:
                    self.x += 2
            case Direction.LEFT:
                _, min_value = min(self.body, key=lambda pos: pos[1])
                _, limit = TOP_LEFT_CORNER
                if self.x - min_value > limit:
                    self.x -= 2
            case _:
                raise ValueError(f"Invalid translation {direction}")

    def display(self, screen: window):
        screen.clear()
        screen.attron(self.color)
        for y, x in self.body:
            screen.addstr(self.y + y, self.x + x, BLOCK)
        screen.refresh()
        screen.attroff(self.color)



