import curses
from typing import Tuple


from snake.snake import Snake 
from _curses import window
from snake.stage import Stage
from snake.utils import Direction, Keys, SNAKE_FOOD
from random import randint
from consts import LINES, COLS

FPS: int = 64

class Game:
    def __init__(self) -> None:

        self.GAME_WINDOW: window = curses.newwin(
            LINES - 1, COLS - 1, 0, 0
        )

        self.GAME_WINDOW.keypad(True)
        self.GAME_WINDOW.nodelay(True)

        self.old_visibility: int = curses.curs_set(0)

    def set_theme(self, color_pair: int) -> None:
        self.GAME_WINDOW.bkgd(' ', color_pair)


    def start(self, stage: Stage) -> None:

        snake: Snake = Snake()
        direction: Direction = Direction.RIGHT 
        food: Tuple[int, int] = self.get_food(snake, stage)
        score: int = 0

        while True:
            head: Tuple[int, int] = snake.get_head()

            new_head: Tuple[int, int] = self.get_position(
                head, direction
            )

            if snake.body.get(new_head, False):
                break 
            if stage.edge.get(new_head, False):
                break

            snake.grow(new_head)

            if not self.is_food_eaten(new_head, food):
                snake.remove_tail()
            else:
                score += 1
                food = self.get_food(snake, stage)

            self.GAME_WINDOW.clear()

            stage.draw(self.GAME_WINDOW)
            
            """self.GAME_WINDOW.addstr(
                0, 0, f"Score: {score}".center(COLS),
                curses.A_BOLD
            )"""
            self.GAME_WINDOW.addstr(
                food[0], food[1], SNAKE_FOOD
            )

            snake.draw(self.GAME_WINDOW)

            self.GAME_WINDOW.refresh()

            key: int = self.GAME_WINDOW.getch()

            curses.napms(FPS)

            match key:
                case Keys.UP:
                    if direction.name != "DOWN":
                        direction = Direction.UP 
                case Keys.DOWN:
                    if direction.name != "UP":
                        direction = Direction.DOWN 
                case Keys.RIGHT:
                    if direction.name != "LEFT":
                        direction = Direction.RIGHT
                case Keys.LEFT:
                    if direction.name != "RIGHT":
                        direction = Direction.LEFT 
                case Keys.ESC:
                    #display_menu()
                    pass
            self.GAME_WINDOW.touchwin()
        curses.curs_set(self.old_visibility)


    def get_food(self, snake: Snake, stage: Stage) -> Tuple[int, int]:
        while True:
            food_y: int = randint(0, LINES - 3)
            food_x: int = randint(0, COLS  - 3)
            food = (food_y, food_x)
            if snake.body.get(food, None):
                continue
            if stage.edge.get(food, None):
                continue
            
            return food 


    def get_position(self, head: Tuple[int, int], delta: Direction) -> Tuple[int, int]:

        new_y: int = ( head[0] + delta.y ) % (LINES -2) 
        new_x: int = ( head[1] + delta.x ) % (COLS - 2) 

        return (new_y, new_x) 


    def is_food_eaten(self, *args: Tuple[int, int]) -> bool:
        head, food = args

        hy, hx = head
        fy, fx = food

        dx = hx - fx

        return hy == fy and 0 <= dx <= 3
        
        # return head == food


