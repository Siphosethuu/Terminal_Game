import curses
# import random

from tile import Tile
from _curses import window
from consts import LINES, COLS
from random import randint
from math import ceil
#from memory.faces import FACES

def main(stdscr: window) -> None:
    memory_game()
    stdscr.getch()


def memory_game() -> None:
    old_visibility: int = curses.curs_set(0)

    GAME_WINDOW: window = curses.newwin(
        LINES, COLS, 0, 0
    )
    GAME_WINDOW.keypad(True)
    _, OLD = curses.mousemask(
        curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION
    )

    GAME_WINDOW.clear()

    while True:
        tiles: list[Tile] = []

        play_round( GAME_WINDOW, tiles )
        if tiles:
            break 
    curses.mousemask(OLD)
    curses.curs_set(old_visibility)



def play_round(game_window: window, tiles: list[Tile]) -> None:

    faces: list[str] = [item for item in "📊📈📉📅📔📒📘📙📚🍏🍎🫐🍒🥭"] * 2

    player_move: int = len(faces) + 1 

    HEIGHT: int = ceil(len(faces) ** 0.5)
    WIDTH : int = (len(faces) // HEIGHT) * Tile.WIDTH

    start_y: int = (LINES - HEIGHT) // 2
    start_x: int = ( COLS -  WIDTH) // 2


    for y in range(start_y, start_y + HEIGHT):
        for x in range(start_x, start_x + WIDTH, Tile.WIDTH):
            tiles.append(
                Tile(
                    faces.pop(
                        randint(0, len(faces) - 1)
                    ),
                    y, x
                )
            )
    flippedtiles: list[Tile] = []

    while True:

        game_window.clear()

        for tile in tiles:
            game_window.addstr(tile.y, tile.x, f"{tile}")

        game_window.touchwin()

        key: str = game_window.getkey()
        
        if key != "KEY_MOUSE":
            continue
            
        try:
            _, x, y, _, bttn_state = curses.getmouse()
        except:
            continue
        if bttn_state & curses.BUTTON1_CLICKED:
            for tile in tiles:
                if tile.is_face_up:
                    continue
                elif tile.is_clicked((y, x)):
                    tile.is_face_up = True
                    flippedtiles.append(tile)
                    if len(flippedtiles) == 2:
                        one, two = flippedtiles
                        if one.face != two.face:
                            one.is_face_up = False
                            two.is_face_up = False
                        flippedtiles = []
                        player_move -= 1 
        if all(tile.is_face_up for tile in tiles):
            break
        elif player_move == 0:
            break



if __name__ == "__main__":
    curses.wrapper(main)
