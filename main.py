import sys

from snake.utils import get_tunnel_stage
from snake.game import Game

import curses

def main(stdscr: curses.window) -> None:
    curses.start_color()


    stdscr.addstr(0, 0,f"{play_snake()}" , curses.A_BOLD)
    sys.exit("Game should be done.")

def play_snake() -> str:
    game: Game = Game()
    return game.start( get_tunnel_stage() )

if __name__ == "__main__":
    curses.wrapper(main)

