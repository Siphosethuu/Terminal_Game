import sys
import json
import curses
import os.path as path



from math import ceil
from curses import window
from random import shuffle
from typing import Dict, List, Tuple
from memory.tile import Tile


from consts import COLS, LINES

FOLDER: str = path.abspath(path.dirname(__file__))
ASSETS: str = path.join(FOLDER, "assets.json")


class Game:
    def __init__(self) -> None:
        self._round: int = 5 

        self.screen: window = curses.newwin(
            LINES, COLS, 0, 0
        )


    
    def start(self) -> None:
        self.get_tiles()
        while True:
            self.display()
            self.screen.getch()
            break


    def display(self) -> None:
        self.screen.erase()
        for tile in self.tiles:
            self.screen.addstr(tile.y, tile.x, f"{tile}")
        self.screen.refresh()

            

    def round_config(self) -> Tuple[int, int, int]:
        num_of_faces: int = ceil(
                pow(self._round + 1, 1.5)
        )

        height: int = int(pow(num_of_faces * 2, 0.5))

        width: int = int(num_of_faces * 2 / height)

        return height, width, num_of_faces


    def get_faces(self, num: int) -> List[str]:
        global ASSETS

        try:
            with open(ASSETS, 'r') as file:
                faces: List[str] = []
                data: Dict[str, List[str]] = json.load(file)["faces"]
                for _, items in data.items():
                    faces.extend(items)
                    if len(faces) >= num:
                        return faces * 2
                else:
                    raise ValueError(
                        f"Congragulations!! You have won the game."
                    )

        except FileNotFoundError as e:
            sys.exit(f"ERROR: {e}")



    def get_tiles(self) -> None:
        self.tiles: List[Tile] = []

        height, width, faces_num = self.round_config()

        faces = self.get_faces(faces_num)

        start_y: int = (LINES - height) // 2

        start_x: int = (COLS  - width * 3) // 2
        
        shuffle(faces)

        for y in range(0, height):
            for x in range(0, width):
                self.tiles.append(
                    Tile(
                        faces.pop(),
                        start_y + y, start_x + x
                    )
                )

