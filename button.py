



from typing import Tuple


class Button:
    WIDTH: int = 3
    def __init__(self, y: int, x: int) -> None:
        self.y = y
        self.x = x


    def is_clicked(self, mouse_pos: Tuple[int, int]) -> bool:
        y, x = mouse_pos
        

        return self.y == y and self.x <= x < self.x + Button.WIDTH


    def __str__(self) -> str:
        raise NotImplementedError(
            f"__str__ function must be implemented by child class ({self.__class__.__name__})."
        )

    def __repr__(self) -> str:
        raise NotImplementedError(
            f"__repr__ method must be implemented by child class ({self.__class__.__name__})."
        )




