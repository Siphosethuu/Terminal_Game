


from typing import Dict, Tuple
from _curses import window 

BLOCK: str = '🟫'


class Stage:
    def __init__(self, edge: Dict[Tuple[int, int], str]) -> None:
        self.edge = edge

    def draw(self, game_window: window) -> None:
        for y, x in self.edge:
            game_window.addstr(y, x, BLOCK)
