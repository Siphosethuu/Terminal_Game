import sys

from snake.utils import get_half_world_stage
from snake.game import Game as Snake
from memory.game import Game as Memory

import curses

def main(stdscr: curses.window) -> None:
    curses.start_color()
    play_memory()


    stdscr.addstr(0, 0,f"{play_snake()}" , curses.A_BOLD)
    sys.exit("Game should be done.")

def play_snake() -> str:
    game: Snake = Snake()
    return game.start( get_half_world_stage() )

def play_memory() -> None:
    old_cursor: int = curses.curs_set(0)
    curses.mousemask(
        curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION
    )
    game: Memory = Memory()
    game.start()


if __name__ == "__main__":
    curses.wrapper(main)

