import curses
from typing import Tuple

from snake.food import Food
from snake.snake import Snake 
from _curses import window
from snake.stage import Stage
from snake.utils import BODY_PART
from consts import COLS, hide_cursor



FPS: int = 100

class Game:
    def __init__(self, screen: window) -> None:

        self.screen = screen

        self.screen.keypad(True)
        self.screen.nodelay(True)



    def set_theme(self, color_pair: int) -> None:
        self.screen.bkgd(' ', color_pair)


    @hide_cursor() # type: ignore
    def start(self, stage: Stage) -> str:

        snake: Snake = Snake(self.screen)
        Food.set_valid_ranges(snake)
        self.food: Tuple[int, int] = Food.food(snake, stage)
        self.score: int = 0
        snake.draw()
        self.draw_food()
        while True:
            snake.grow()

            head: Tuple[int,int] = snake.get_head()
            if snake.bit_itself():
                return f"Bit yourself at {head}." 
            if snake.crashed(stage):
                return f"Hit edge at {head}."

    
            has_eaten = Food.is_food_eaten(head, self.food)
            snake.move(has_eaten)
            if has_eaten:
                self.score += 1
                self.food = Food.food(snake, stage)
                self.draw_food()

            self.display_score()

            snake.input()
            self.screen.refresh()



    def display_score(self) -> None:
        global COLS

        msg: str = f"Score: {self.score}"
        x: int = ( COLS - len(msg) ) // 2
        self.screen.move(0, 0)
        self.screen.clrtoeol()
        self.screen.addstr(0, x, msg, curses.A_STANDOUT)

    def draw_food(self) -> None:
       self.screen.addstr(
            self.food[0], self.food[1], BODY_PART,
            curses.A_STANDOUT
        )

