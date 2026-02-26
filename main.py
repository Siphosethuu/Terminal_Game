

from snake.stage import Stage
from snake.utils import get_box_stage 
from snake.game import Game

import curses

def main(stdscr: curses.window) -> None:
    curses.start_color()

    stdscr.addstr(0, 0, f"WELCOME!!!", curses.A_BOLD)

    play_snake()

    stdscr.getch()

def play_snake() -> None:
    game: Game = Game()
    game.start(
        Stage( get_box_stage() )
    )

if __name__ == "__main__":
    curses.wrapper(main)
