
from typing import Tuple
from consts import Direction, BLOCK
from curses import A_CHARTEXT, window
from tetris.utils import *




class Shape:
    #screen: window = None

    @classmethod
    def set_screen(cls, screen: window) -> None:
        Shape.screen = screen

    
    def __init__(self, shape: str) -> None:
        self.shape = shape
        self.reset()


    def reset(self) -> None:
        self.y, self.x = 3, 12
        self.rotation: int = 0
        self.is_grounded: bool = False


    def is_valid_dir(self, delta: Direction) -> bool:
        global SHAPES

        body: set[Tuple[int, int]] = SHAPES[self.shape][self.rotation]
        for y, x in body:
            new_y, new_x = delta.y + y, delta.x + x
            if (new_y, new_x) in body:
                continue
            to_y,to_x = new_y + self.y, new_x + self.x
            char: int = Shape.screen.inch(to_y, to_x)
            char = char & A_CHARTEXT
            if char == BLOCK or not self.is_within_bounds(to_y, to_x):
                return False
        return True

        


    def fall(self) -> None:
        if self.is_valid_dir(Direction.DOWN):
            self.y += 1
        else:
            Shape.screen.addstr(0, 0, f"{self.is_valid_dir(Direction.DOWN) = }")
            self.is_grounded = True

            
    def translate(self, direction: Direction) -> None:
        if self.is_valid_dir(direction):
            self.y = self.y + direction.y 
            self.x = self.x + direction.x 

    def rotate(self) -> None:
        global SHAPES, ROTATION_DIRS

        self.rotation = (self.rotation + 1) % len(
                SHAPES[self.shape])
        for delta in ROTATION_DIRS:
            if self.is_valid_dir(delta):
                return
        self.rotation = (self.rotation - 1 )  % len(
                SHAPES[self.shape])


    def display(self):
        global SHAPES
        for y, x in SHAPES[self.shape][self.rotation]:
            Shape.screen.addstr(self.y+y, self.x+x, BLOCK)

    def is_within_bounds(self, to_y: int, to_x: int) -> bool:
        top, left = TOP_LEFT_CORNER
        bottom, right = BOTTOM_RIGHT_CORNER
        return top < to_y < bottom and left < to_x < right



