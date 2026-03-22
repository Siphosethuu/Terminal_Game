
from consts import Keys
from typing import Tuple
from consts import Direction
from curses import A_ATTRIBUTES, napms, window
from tetris.utils import *






class Shape:
    
    def __init__(self, shape: str, screen: window, attribute: int) -> None:
        self.shape = shape
        self.screen = screen
        self.bkgd_attr: int = self.screen.getbkgd() & A_ATTRIBUTES # type: ignore
        self.attribute = attribute

        self.reset()


    @property
    def rotations(self)-> List[set[Tuple[int, int]]]:
        global SHAPES

        return SHAPES[self.shape]["ROTATIONS"]


   
    @property
    def body(self) -> set[Tuple[int, int]]:
        return self.rotations[self.rotation]



    def reset(self) -> None:
        self.y, self.x = 10, 10
        self.rotation: int = 0
        self.is_grounded: bool = False


    def is_another_piece_obstructing(self, delta: Direction) -> bool:
        for pos_y, pos_x in self.body:
            y: int = pos_y + delta.y
            x: int = pos_x + delta.x
            if (y, x) in self.body:
                continue

            to_y: int = y + self.y 
            to_x: int = x + self.x

            attr: int = self.screen.inch(to_y, to_x) & A_ATTRIBUTES
            
            if attr != self.bkgd_attr:
                return True
        return False

            
        


    def translate(self, direction: Direction) -> bool:
        if self.is_another_piece_obstructing(direction) or not self.is_within_bounds():
            return False

        self.display(self.bkgd_attr)
        self.y += direction.y
        self.x += direction.x
        self.display(self.attribute)
        return True

    
    def fall(self) -> None:
        if not self.translate(Direction.DOWN):
            self.is_grounded = True


    def input(self) -> None:
        key: int = self.screen.getch()
        napms(84)
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
                pass

    def rotate(self) -> None:
        global SHAPES


        self.display(self.bkgd_attr)

        self.rotation = (self.rotation + 1) % len(
            self.rotations)
        for delta in (Direction.NONE, Direction.RIGHT, Direction.LEFT):
            self.y += delta.y
            self.x += delta.x
            if not self.is_another_piece_obstructing(delta):
                self.display(self.attribute)
                return
            self.y -= delta.opposite.y
            self.x -= delta.opposite.x

        self.rotation = (self.rotation - 1 )  % len(
            self.rotations)


    def display(self, attributes: int ) -> None:
        self.screen.attron(attributes)
        for y, x in self.body:
            self.screen.addstr(
                self.y + y, self.x + x, "  ",
            )
        self.screen.attroff(attributes)

    
    def is_within_bounds(self, to_y: int | None= None, to_x: int | None = None) -> bool:

        to_y = to_y if not to_y is None else self.y
        to_x = to_x if not to_x is None else self.x

        top, left = TOP_LEFT_CORNER
        bottom, right = BOTTOM_RIGHT_CORNER
        return top < to_y < bottom and left < to_x < right




    @classmethod
    def create_shapes(cls, screen: window) -> List["Shape"]:
        global SHAPES

        shapes: List[Shape] = []
        for shape in SHAPES:
            attr: int = SHAPES[shape]["COLOR"]
            for _ in range(0, 3):
                shapes.append(Shape(
                    shape, screen,
                    curses.color_pair(attr)) 
                )
        return shapes


