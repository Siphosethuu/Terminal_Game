import sys

from snake.utils import get_half_world_stage
from snake.game import Game as Snake
from memory.game import Game as Memory
from tetris.game import Game as Tetris

import curses

def main(stdscr: curses.window) -> None:
    curses.start_color()
    play_tetris()


    # stdscr.addstr(0, 0,f"{play_snake()}" , curses.A_BOLD)
    sys.exit()#"Game should be done.")

def play_snake() -> str:
    game: Snake = Snake()
    return game.start( get_half_world_stage() )

def play_memory() -> None:
    game: Memory = Memory()
    game.start()
    curses.curs_set(game.old_curs_set)
    curses.mousemask(game.old_mousemask)


def play_tetris() -> None:
    game: Tetris = Tetris()
    game.start()


if __name__ == "__main__":
    curses.wrapper(main)

