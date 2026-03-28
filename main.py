import sys
from typing import List

from consts import BLOCK, COLS, LINES
from snake.utils import get_empty_world, get_half_world_stage
from snake.game import Game as Snake
from memory.game import Game as Memory
from tetris.game import Game as Tetris

import curses
ORANGE: int = 8 
def main(stdscr: curses.window) -> None:
    curses.start_color()

    curses.init_color(ORANGE, 1000, 647, 0) 
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_BLUE)
    curses.init_pair(3, curses.COLOR_BLACK, ORANGE) 
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_RED)
    curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_MAGENTA)
    curses.init_pair(7, curses.COLOR_BLACK, curses.COLOR_YELLOW)

    curses.init_pair(8, curses.COLOR_BLACK, curses.COLOR_CYAN)
    stdscr.bkgd(' ', curses.color_pair(1))
    play_tetris(stdscr)


    # stdscr.addstr(0, 0,f"{play_snake()}" , curses.A_BOLD)
    sys.exit()#"Game should be done.")





def play_snake(stdscr: curses.window) -> str:
    game: Snake = Snake(stdscr)
    #game.set_theme(theme)
    game.start( get_empty_world(stdscr) )
    return "Won or Lost."

def play_memory() -> None:
    game: Memory = Memory()
    game.start()
    curses.curs_set(game.old_curs_set)
    curses.mousemask(game.old_mousemask)


def play_tetris(stdscr: curses.window) -> None:

  
    game: Tetris = Tetris(stdscr)
    game.start()
    #curses.napms(5000)


if __name__ == "__main__":
    curses.wrapper(main)

