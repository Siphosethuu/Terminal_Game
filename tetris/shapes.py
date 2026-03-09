
from typing import Tuple
from consts import Direction, BLOCK
from curses import A_CHARTEXT, window
from tetris.utils import *




class Shape:
    
    def __init__(self, shape: str) -> None:
        self.shape = shape
        self.reset()

    @property
    def body(self) -> set[Tuple[int, int]]:
        global SHAPES

        return SHAPES[self.shape][self.rotation]

    def reset(self) -> None:
        self.y, self.x = 5, 12
        self.rotation: int = 0
        self.is_grounded: bool = False


    def is_valid_dir(self, delta: Direction, screen: window) -> bool:
        for y, x in self.body:
            new_y, new_x = delta.y + y, delta.x + x
            if (new_y, new_x) in self.body:
                continue
            to_y,to_x = new_y + self.y, new_x + self.x
            char: int = screen.inch(to_y, to_x)
            char = char & A_CHARTEXT
            if char == BLOCK or not self.is_within_bounds(to_y, to_x):
                return False
        return True

        


    def fall(self, screen: window) -> None:
        if self.is_valid_dir(Direction.DOWN, screen):
            self.y += 1
        else:
            self.is_grounded = True

            
    def translate(self, direction: Direction, screen: window) -> None:
        if self.is_valid_dir(direction, screen):
            self.y = self.y + direction.y 
            self.x = self.x + direction.x 

    def rotate(self, screen: window) -> None:
        global SHAPES, ROTATION_DIRS

        self.rotation = (self.rotation + 1) % len(
                SHAPES[self.shape])
        for delta in ROTATION_DIRS:
            if self.is_valid_dir(delta, screen):
                return
        self.rotation = (self.rotation - 1 )  % len(
                SHAPES[self.shape])


    def display(self, screen: window):
        # screen.attron(COLORS[self.shape])
        for y, x in self.body:
            screen.addstr(
                self.y+y, self.x+x, BLOCK,
                COLORS[self.shape])
        # screen.attroff(COLORS[self.shape])

    def is_within_bounds(self, to_y: int, to_x: int) -> bool:
        top, left = TOP_LEFT_CORNER
        bottom, right = BOTTOM_RIGHT_CORNER
        return top < to_y < bottom and left < to_x < right



