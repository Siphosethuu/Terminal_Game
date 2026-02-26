import os
import sys

# Get the absolute path of the parent directory (project root)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the project root to sys.path
sys.path.append(project_root)

# Now you can import the module from the root directory


from button import Button
from utils import DEFAULT_FACE



class Tile(Button):
    def __init__(self, face: str, y: int, x: int) -> None:
        super().__init__(y, x)

        self.is_face_up: bool = False
        self.face = face

    def __str__(self) -> str:
        global DEFAULT_FACE

        if self.is_face_up:
            return self.face.center(self.WIDTH)
        return DEFAULT_FACE.center(self.WIDTH)

    def __repr__(self) -> str:
        return f"Tile({str(self)})"
