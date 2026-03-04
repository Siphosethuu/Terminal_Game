import sys
import json
import time
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
        self._round: int = 6 

        self.screen: window = curses.newwin(
            LINES, COLS, 0, 0
        )
        self.screen.keypad(True)
        self.old_curs_set: int = curses.curs_set(0)
        _, self.old_mousemask = curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)


    
    def start(self) -> None:
        self.get_tiles()
        self.player_moves: int = len(self.tiles) + 5
        flipped: List[Tile] = []
        while True:
            self.display()
            key: str = self.screen.getkey()
            if key != "KEY_MOUSE":
                continue
            try:
                _, x, y, _, btnstate = curses.getmouse()
            except Exception as e:
                print(f"ERROR: {e}.")
                continue

            if not btnstate & curses.BUTTON1_CLICKED:
                continue
            for tile in self.tiles:
                if tile.is_face_up:
                    continue
                if not tile.is_clicked((y, x)):
                    continue
                tile.is_face_up = True
                flipped.append(tile)
                if len(flipped) == 2:
                    first, second = flipped
                    if first.face != second.face:
                        self.display()
                        curses.napms(500)
                        first.is_face_up = False
                        second.is_face_up = False
                    flipped = []
                    self.player_moves -= 1
                break



    def display(self) -> None:
        self.screen.erase()
        for tile in self.tiles:
            self.screen.addstr(tile.y, tile.x, f" {tile} ")
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
                        return faces
                else:
                    raise ValueError(
                        f"Congragulations!! You have won the game."
                    )

        except FileNotFoundError as e:
            sys.exit(f"ERROR: {e}")



    def get_tiles(self) -> None:
        self.tiles: List[Tile] = []

        height, width, faces_num = self.round_config()

        faces = self.get_faces(faces_num)[:faces_num]
        faces *= 2

        start_y: int = (LINES - height) // 2

        start_x: int = (COLS  - (width * 3)) // 2
        
        shuffle(faces)

        for y in range(start_y, start_y + height):
            for x in range(start_x, start_x + (width * 3), 3):
                self.tiles.append(
                    Tile(
                        faces.pop(),
                        y, x)
                )

