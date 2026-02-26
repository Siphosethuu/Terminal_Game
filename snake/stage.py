



from typing import Dict, Tuple
from curses import color_pair, init_pair, window, COLOR_BLUE, COLOR_MAGENTA

BLOCK: str = ' '


class Stage:
    def __init__(self, edge: Dict[Tuple[int, int], int]) -> None:
        self.edge = edge
        init_pair(1, COLOR_BLUE, COLOR_MAGENTA)
        self.color: int = color_pair(1)

    def draw(self, game_window: window) -> None:
        game_window.attron(self.color)
        try:
            for y, x in self.edge:
                game_window.addstr(y, x, BLOCK)
        except Exception:
            pass
        game_window.attroff(self.color)
