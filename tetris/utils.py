


from typing import Tuple
from consts import COLS, LINES

WIDTH: int = 20
HEIGHT: int = 40


x: int = ( COLS - WIDTH ) // 2
y: int = (LINES - HEIGHT ) // 2

TOP_LEFT_CORNER: Tuple[int, int] = (y, x)
BOTTOM_RIGHT_CORNER: Tuple[int, int] = (y + HEIGHT, x + WIDTH)


