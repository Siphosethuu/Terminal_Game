
from button import Button
from memory.utils import DEFAULT_FACE



class Tile(Button):
    def __init__(self, face: str, y: int, x: int) -> None:
        super().__init__(y, x)

        self.is_face_up: bool = False

        self.face = face

    def __str__(self) -> str:
        global DEFAULT_FACE

        if self.is_face_up:
            return self.face
        return DEFAULT_FACE

    def __repr__(self) -> str:
        return f"Tile({str(self)})"
