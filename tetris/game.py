import curses

from typing import List
from tetris.shape import Shape
# from tetris.utils import TOP_LEFT_CORNER, BOTTOM_RIGHT_CORNER
from random import randint, shuffle
from consts import hide_cursor, draw_square_boundary, clear

shapes: List[str] = ['L', 'J', 'Z', 'S', 'T', 'O']
class Game:
    def __init__(self, screen: curses.window) -> None:
        self.screen = screen
        Shape.init_screen(self.screen)
        self.shapes: List[Shape] = Shape.create_shapes()
        self.score: int = 0
        self.is_running: bool = True
        self.screen.nodelay(True)
        self.screen.keypad(True)


    @hide_cursor
    def start(self) -> None:

        self.next_shapes: List[Shape] = [ ]
        for _ in range(0, 3):
            shuffle(self.shapes)
            self.next_shapes.append(self.shapes.pop(0))

        shape: Shape = self.shapes.pop()
        shape.reset()

        draw_square_boundary(self.screen, Shape.top, Shape.left, Shape.bottom, Shape.right)

        self.top_left = (Shape.top + 4, Shape.right + 8)
        self.bottom_right = (Shape.bottom - 4, Shape.right + 8 + 12)
        draw_square_boundary(self.screen, *self.top_left, *self.bottom_right)
        self.draw_next_shapes()

        while self.is_running:
            if shape.is_grounded:
                if shape.min_y + shape.y <= Shape.top:
                    break
                self.recycle_shape(shape)
                self.update_waiting_list()
                shape = self.get_shape()
                self.draw_next_shapes()
            shape.input()
            shape.falling_effect.update()
            shuffle(self.shapes)

    

    def get_shape(self) -> Shape:
        shape: Shape = self.next_shapes.pop(0)
        shape.reset()
        return shape

    
    def recycle_shape(self, shape: Shape) -> None:
        self.shapes.insert(randint(0, len(self.shapes)), shape)

    
    def update_waiting_list(self):
        self.next_shapes.append(self.shapes.pop(0))


    def draw_next_shapes(self) -> None:
        top, left = self.top_left
        bottom, right = self.bottom_right

        clear(self.screen,top, left, bottom, right)

        MID_X: int = (left + right - 2) // 2
        L: int = bottom - top
        N: int = len(self.next_shapes)
        for i, shape in enumerate(self.next_shapes, start=0):
            shape.reset()
            mid_x: int = (shape.min_x + shape.max_x) // 2
            mid_y: int = (shape.min_y + shape.max_y) // 2
            mid: int = int(2 * top + i * L / N + (i + 1) * L / N) // 2
            shape.pos =  mid - mid_y, MID_X - mid_x
            shape.draw()




    

