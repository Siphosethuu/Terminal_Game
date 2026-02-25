import curses
from typing import Tuple


from snake.snake import Snake 
from _curses import window
from utils import SnakeDirection, Keys
from random import randint

SNAKE_FOOD: str = '██'

FPS: int = 64


def play_snake() -> None:
    snake: Snake = Snake()
    game_window: window = curses.newwin(
        curses.LINES - 1, curses.COLS - 1, 0, 0
    )
    curses.init_pair(
        1, curses.COLOR_BLACK, curses.COLOR_GREEN
    )
    
    curses.init_pair(
        2, curses.COLOR_BLUE, curses.COLOR_GREEN
    )
    curses.init_pair(
        3, curses.COLOR_WHITE, curses.COLOR_GREEN
    )
    

    game_window.bkgd(' ', curses.color_pair(1))

    direction: Tuple[int, int] = SnakeDirection.RIGHT
    
    food: Tuple[int, int] = get_food(snake)

    game_window.keypad(True)
    game_window.nodelay(True)

    old_visibility: int = curses.curs_set(0)

    while True:

        old_head: Tuple[int, int] = snake.get_head()

        new_head = get_position(*old_head, *direction)
        game_over: bool = snake.body.get(
            new_head, None
        ) is None

        if not game_over:
            break

        snake.grow(new_head)

        if not is_food_eaten(*new_head, *food):
            snake.remove_tail()
        else:
            food = get_food(snake)

        game_window.clear()

        game_window.addstr(
            food[0], food[1], SNAKE_FOOD
        )

        # game_window.attron(curses.color_pair(3))
        snake.draw(game_window)
        # game_window.attroff(curses.color_pair(3))

        key: int = game_window.getch()

        curses.napms(FPS)

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


def get_food(snake: Snake) -> Tuple[int, int]:
    while True:
        food_y: int = randint(0, curses.LINES - 2)
        food_x: int = randint(0, curses.COLS  - 2)
        food = (food_y, food_x)
        if not snake.body.get(food, None):
            return food



def get_position(*args: int) -> Tuple[int, int]:
    y, x, dy, dx = args

    new_y: int = y + dy
    if new_y >= curses.LINES - 1:
        new_y = 0
    elif new_y < 0:
        new_y = curses.LINES - 2

    new_x: int = x + dx
    if new_x >= curses.COLS - 1:
        new_x = 0
    elif new_x < 0:
        new_x = curses.COLS - 2

    return (new_y, new_x)



def is_food_eaten(*args: int) -> bool:
    hy, hx, fy, fx = args

    dy, dx = abs(hy - fy), abs(hx - fx)

    return 0 <= dy <= 1 and 0 <= dx <= 1


