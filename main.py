import curses
from typing import Tuple


from snake import Snake 
from _curses import window
from utils import SnakeDirection, Keys
from random import randint



def main(stdscr: window) -> None:
    curses.start_color()
    stdscr.addstr(
        0, 0,
        "Terminal Games:".center(curses.COLS - 1),
        curses.A_BOLD | curses.A_STANDOUT
    )
    play_snake()
    stdscr.touchwin()

    stdscr.getch()

def play_snake() -> None:
    snake: Snake = Snake()
    game_window: window = curses.newwin(
        curses.LINES - 1, curses.COLS - 1, 0, 0
    )
    curses.init_pair(
        1, curses.COLOR_BLACK, curses.COLOR_GREEN
    )
    curses.init_color(1, 255, 255, 255)
    curses.init_pair(
        2, curses.COLOR_BLACK, curses.COLOR_RED
    )
    curses.init_pair(
        3, curses.COLOR_BLACK, curses.COLOR_WHITE
    )
    

    game_window.bkgd(' ', curses.color_pair(1))
    direction: Tuple[int, int] = SnakeDirection.RIGHT
    food: Tuple[int, int] = get_food(snake)

    game_window.keypad(True)
    game_window.nodelay(True)
    old_visibility: int = curses.curs_set(0)
    while True:
        dy, dx = direction

        old_y, old_x = snake.get_head()

        new_head = (old_y + dy, old_x + dx)

        val = snake.body.get(new_head, None)

        if not val is None:
            break

        snake.grow(new_head)
        if food != new_head:
            snake.remove_tail()
        else:
            food = get_food(snake)
        game_window.clear()
        game_window.attron(curses.color_pair(2))
        game_window.addch(food[0], food[1], ' ',)
        game_window.attroff(curses.color_pair(2))

        game_window.attron(curses.color_pair(3))
        for y, x in snake.body:
            game_window.addch(y, x, ' ')
        game_window.attroff(curses.color_pair(3))

        key: int = game_window.getch()
        curses.napms(100)

        match key:
            case Keys.UP:
                if direction != SnakeDirection.DOWN:
                    direction = SnakeDirection.UP
            case Keys.DOWN:
                if direction != SnakeDirection.UP:
                    direction = SnakeDirection.DOWN
            case Keys.RIGHT:
                if direction != SnakeDirection.LEFT:
                    direction = SnakeDirection.RIGHT
            case Keys.LEFT:
                if direction != SnakeDirection.RIGHT:
                    direction = SnakeDirection.LEFT
            case Keys.ESC:
                #display_menu()
                pass
        game_window.touchwin()
    curses.curs_set(old_visibility)
    game_window.getch()


def get_food(snake: Snake) -> Tuple[int, int]:
    while True:
        food_y: int = randint(0, curses.LINES - 1)
        food_x: int = randint(0, curses.COLS - 1)
        food = (food_y, food_x)
        if not snake.body.get(food, None):
            return food



if __name__ == "__main__":
    curses.wrapper(main)


