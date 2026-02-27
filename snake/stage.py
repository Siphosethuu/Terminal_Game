



from typing import Dict, Tuple
from curses import color_pair, init_pair, window, COLOR_BLUE, COLOR_MAGENTA



class Stage:
    def __init__(self, edge: Dict[Tuple[int, int], str]) -> None:
        self.edge = edge
        init_pair(1, COLOR_BLUE, COLOR_MAGENTA)
        self.color: int = color_pair(1)

    def draw(self, game_window: window) -> None:
        game_window.attron(self.color)
        for pos, block in self.edge.items():
            y, x = pos
            try:
                game_window.addstr(y, x, block)
            except Exception:
                pass
        game_window.attroff(self.color)

    def overlaps(self, pos: Tuple[int, int]) -> bool:
        return not self.edge.get(pos, None) is None
