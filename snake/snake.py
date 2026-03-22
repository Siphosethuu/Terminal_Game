from collections import OrderedDict
from typing import List, Tuple
from consts import Direction, Keys
from snake.utils import LINES, COLS, BODY_PART
from curses import A_ATTRIBUTES, A_CHARTEXT, napms, window, A_REVERSE
from snake.stage import Stage



class Snake():
    def __init__(self, screen: window) -> None:
        self.body: List[Tuple[int, int]] = []
        self.screen = screen
        self.direction: Direction = Direction.RIGHT
        info: int = self.screen.getbkgd()
        self.bkgd_char: str = chr(info & A_CHARTEXT)
        self.bkgd_attr: int = info & A_ATTRIBUTES
        self.reset(5)


    def reset(self, _size: int) -> None:
        global LINES, COLS

        self.body.clear()
        head_y: int = LINES // 2
        head_x: int = ( COLS - _size ) // 2
        for body_x in range(head_x, head_x - _size, -2):
            self.body.append((head_y, body_x))


    def grow(self) -> None:
        y, x = self.get_head() 
        new_head = ( y + self.direction.y, x + self.direction.x )
        self.body.insert(0, new_head)


    def get_tail(self) -> Tuple[int, int]:
        return self.body.pop()


    def get_head(self) -> Tuple[int, int]:
        return self.body[0]

    def overlaps(self, pos: Tuple[int, int]) -> bool:
        return pos in self.body

    def draw(self) -> None:
        global BODY_PART

        for y, x in self.body:
            self.screen.addstr(y, x, BODY_PART, A_REVERSE)

    
    def move(self, has_eaten: bool):
        global BODY_PART


        y, x = self.get_head()
        self.screen.addstr(y, x, BODY_PART, A_REVERSE)

        if not has_eaten:
            y, x = self.get_tail()
            self.screen.addstr(
                y, x, BODY_PART, 
                self.bkgd_attr
            )


    def bit_itself(self) -> bool:
        return self.body.count(self.get_head()) >= 2



    def crashed(self, stage: Stage) -> bool:
        return self.get_head() in stage.edge



    def input(self) -> None:
        key: int = self.screen.getch()
        napms(200)
        match key:
            case Keys.UP | 119 | 87:
                if self.direction.name != "DOWN":
                    self.direction = Direction.UP 
            case Keys.DOWN | 115 | 83:
                if self.direction.name != "UP":
                    self.direction = Direction.DOWN 
            case Keys.RIGHT | 100 | 68:
                if self.direction.name != "LEFT":
                    self.direction = Direction.RIGHT
            case Keys.LEFT | 97 | 65:
                if self.direction.name != "RIGHT":
                    self.direction = Direction.LEFT 
            case Keys.ESC:
                #Display Menu
                pass
