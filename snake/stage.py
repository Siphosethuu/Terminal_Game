



from typing import Dict, Tuple
from curses import window



class Stage:
    def __init__(self, edge: Dict[Tuple[int, int], str], screen: window) -> None:
        self.edge = edge
        self.attribute: int = 67
        self.screen = screen
    
    def draw(self) -> None:
        self.screen.attron(self.attribute)
        for pos, block in self.edge.items():
            y, x = pos
            try:
                self.screen.addstr(y, x, block)
            except Exception:
                pass
        self.screen.attroff(self.attribute)

    
    def overlaps(self, pos: Tuple[int, int]) -> bool:
        return not self.edge.get(pos, None) is None
