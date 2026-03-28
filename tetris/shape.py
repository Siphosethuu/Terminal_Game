


from typing import Tuple
from consts import Direction, Keys
from timer import Timer
from curses import A_ATTRIBUTES, A_CHARTEXT, color_pair, window
from tetris.utils import *


DT: float = 0.485


class Shape:
    top: int = TOP_LEFT_CORNER[0] - 1
    left: int = TOP_LEFT_CORNER[1]
    bottom, right = BOTTOM_RIGHT_CORNER

    def __init__(self, shape: str, attributes: int) -> None:
        global DT
        self.shape = shape
        self.attributes = attributes
        self.falling_effect: Timer = Timer(DT, self.fall)
        

    @property
    def max_y(self) -> int:
        return max(self.body,key=lambda pos: pos[0])[0]

    @property
    def min_y(self) -> int:
        return min(self.body,key=lambda pos: pos[0])[0] 


    @property
    def min_x(self) -> int:
        return min(self.body, key=lambda pos: pos[1])[1]

    @property
    def max_x(self) -> int:
        return max(self.body, key=lambda pos: pos[1])[1]

    @property
    def y(self) -> int:
        return self.pos[0]

    @property
    def x(self) -> int:
        return self.pos[1]

    @property
    def rotations(self)-> List[set[Tuple[int, int]]]:
        global SHAPES

        return SHAPES[self.shape]["ROTATIONS"]


    @property
    def body(self) -> set[Tuple[int, int]]:
        return self.rotations[self.rotation]



    def reset(self) -> None:
        self.pos: Tuple[int, int] = ( Shape.top, 19 )
        self.rotation: int = 0
        self.is_grounded: bool = False
        self.falling_effect.start()


    @staticmethod
    def another_piece_obstructing(pos: Tuple[int, int], body: set[Tuple[int, int]]) -> bool:
        """
        ASSUMES WE FIRST CLEAR THE PREVIOUS STATE DRAWN
        """
        for dy, dx in body:
            y: int = pos[0] + dy
            x: int = pos[1] + dx
            location_info = Shape.screen.inch(y, x)
            if location_info != Shape.bkgd_info:
                return True
        return False
                

            
    @staticmethod
    def is_valid(pos:Tuple[int, int], body: set[Tuple[int, int]]) -> bool:
        return not Shape.another_piece_obstructing( pos, body ) and Shape.is_within_bounds(pos, body)


    @staticmethod
    def apply_translation(pos: Tuple[int, int], direction: Direction, step: int = 1) -> Tuple[int, int]:
        return (pos[0] + (direction.y * step), pos[1] + ( direction.x * step))


    
    def fall(self) -> None:
        pos = Shape.apply_translation(self.pos, Direction.DOWN)
        self.clear()
        if Shape.is_valid(pos, self.body):
            self.pos = pos
            self.falling_effect.start()
        else:
            self.is_grounded = True 
            self.falling_effect.stop()
        self.draw()



    def input(self) -> None:
        key: int = self.screen.getch()
        match key:
            case Keys.UP | 119 | 87:
                self.rotate()
            case Keys.DOWN | 115 | 83:
                self.fall()
            case Keys.RIGHT | 100 | 68:
                self.translate(Direction.RIGHT)
            case Keys.LEFT | 97 | 65:
                self.translate(Direction.LEFT)
            case Keys.ESC:
                # Display Menu
                self.is_grounded = True


    def translate(self, direction: Direction) -> None:
        self.clear()
        pos = Shape.apply_translation(self.pos, direction)

        if Shape.is_valid(pos, self.body):
            self.pos = pos
        self.draw()


    def rotate(self) -> None:
        global ROTATION_DIRECTIONS


        self.clear()
        revert: bool = True
        old_rotation = self.rotation 
        self.rotation = (self.rotation + 1) % len(self.rotations)
        try:
            for delta in ROTATION_DIRECTIONS:
                for step in range(1, 3):
                    pos = Shape.apply_translation(self.pos, delta, step)
                    if self.is_valid(pos, self.body):
                        self.pos = pos
                        revert = False
                        return 
        finally:
            if revert:
                self.rotation = old_rotation
            self.draw()


    def draw(self) -> None:
        self.display(self.pos, "[]", self.attributes)

    def clear(self) -> None:
        self.display(self.pos, "  ", Shape.bkgd_attr)

    def display(self, pos:Tuple, char: str, attributes: int) -> None:
        Shape.screen.attron(attributes)
        for dy, dx in self.body:
            y: int = dy + pos[0]
            x: int = dx + pos[1]
            if y >= Shape.top:
                Shape.screen.addstr(
                    y, x, char
                )
        Shape.screen.attroff(attributes)

    
    @staticmethod
    def is_within_bounds(pos: Tuple[int, int], body: set[Tuple[int, int]]) -> bool:
        for dy, dx in body:
            y: int = dy + pos[0]
            x: int = dx + pos[1]
            if not (y < Shape.bottom and x >= Shape.left and x < Shape.right):
                return False
        return True



    @classmethod
    def create_shapes(cls) -> List["Shape"]:
        global SHAPES

        shapes: List[Shape] = []
        for shape in SHAPES:
            attr = SHAPES[shape]["ATTRIBUTES"]
            for _ in range(0, 3):
                shapes.append(Shape(shape, color_pair(attr)))
        return shapes


    @classmethod
    def init_screen(cls, screen: window) -> None:
        Shape.screen = screen
        Shape.bkgd_info = Shape.screen.getbkgd()
        Shape.bkgd_char: str = chr(Shape.bkgd_info & A_CHARTEXT)
        Shape.bkgd_attr: int = Shape.bkgd_info & A_ATTRIBUTES


