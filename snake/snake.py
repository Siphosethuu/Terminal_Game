from collections import OrderedDict
from typing import Tuple
from snake.utils import LINES, COLS, BODY_PART
from _curses import window



class Snake():
    def __init__(self) -> None:
        self.body: OrderedDict[Tuple[int, int], bool] = OrderedDict()
        self.reset(5)

    def reset(self, _size: int) -> None:
        global LINES, COLS

        self.body.clear()
        head_y: int = LINES // 2
        head_x: int = ( COLS - _size ) // 2
        for body_x in range(head_x, head_x - _size, -1):
            self.body[(head_y, body_x)] = True


    def grow(self, new_head: Tuple[int, int]) -> None:
        self.body[new_head] = True
        self.body.move_to_end(new_head, last=False)


    def remove_tail(self) -> None:
        self.body.popitem(last=True)


    def get_head(self) -> Tuple[int, int]:
        for body_part in self.body:
            return body_part

    def draw(self, canvas: window) -> None:
        global BODY_PART

        for y, x in self.body:
            canvas.addstr(y, x, BODY_PART)
