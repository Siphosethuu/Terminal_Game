import curses
from typing import Tuple


from snake.snake import Snake 
from _curses import window
from snake.stage import Stage
from snake.utils import Keys, SNAKE_FOOD
from random import randint
from consts import LINES, COLS, Direction, hide_cursor



FPS: int = 100

class Game:
    def __init__(self) -> None:

        self.GAME_WINDOW: window = curses.newwin(
            curses.LINES, curses.COLS + 1, 0, 0
        )

        self.GAME_WINDOW.keypad(True)
        self.GAME_WINDOW.nodelay(True)

        self.old_visibility: int = curses.curs_set(0)

    def set_theme(self, color_pair: int) -> None:
        self.GAME_WINDOW.bkgd(' ', color_pair)


    @hide_cursor()
    def start(self, stage: Stage) -> str:

        snake: Snake = Snake()
        direction: Direction = Direction.RIGHT 
        food: Tuple[int, int] = self.get_food(snake, stage)
        score: int = 0

        while True:
            head: Tuple[int, int] = snake.get_head()

            new_head: Tuple[int, int] = self.get_position(
                head, direction
            )

            if snake.overlaps(new_head):
                return f"Bit yourself at {new_head}." 
            if stage.overlaps(new_head):
                return f"Hit edge at {new_head}; ({LINES}, {COLS})."

            new_head = self.wrap_pos(new_head)

            snake.grow(new_head)

            if not self.is_food_eaten(new_head, food):
                snake.remove_tail()
            else:
                score += 1
                food = self.get_food(snake, stage)

            self.GAME_WINDOW.clear()

            stage.draw(self.GAME_WINDOW)
            
            self.GAME_WINDOW.addstr(
                0, 0, f"Score: {score}".center(curses.COLS),
                curses.A_BOLD | curses.A_STANDOUT
            )
            self.GAME_WINDOW.addstr(
                food[0], food[1], SNAKE_FOOD
            )

            snake.draw(self.GAME_WINDOW)

            self.GAME_WINDOW.refresh()

            key: int = self.GAME_WINDOW.getch()

            curses.napms(FPS)

            match key:
                case Keys.UP | 119 | 87:
                    if direction.name != "DOWN":
                        direction = Direction.UP 
                case Keys.DOWN | 115 | 83:
                    if direction.name != "UP":
                        direction = Direction.DOWN 
                case Keys.RIGHT | 100 | 68:
                    if direction.name != "LEFT":
                        direction = Direction.RIGHT
                case Keys.LEFT | 97 | 65:
                    if direction.name != "RIGHT":
                        direction = Direction.LEFT 
                case Keys.ESC:
                    #display_menu()
                    pass
            self.GAME_WINDOW.touchwin()
        #curses.curs_set(self.old_visibility)


    def get_food(self, snake: Snake, stage: Stage) -> Tuple[int, int]:
        while True:
            food_y: int = randint(1, LINES)
            food_x: int = randint(1, COLS )
            food = (food_y, food_x)
            if snake.overlaps(food):
                continue
            if stage.overlaps(food):
                continue
            
            return food 


    def get_position(self, pos: Tuple[int, int], delta: Direction) -> Tuple[int, int]:

        y, x = pos

        new_y: int = ( y + delta.y ) 
        new_x: int = ( x + delta.x )

        return (new_y, new_x) 

    def wrap_pos(self, pos: Tuple[int, int]) -> Tuple[int, int]:

        return ( pos[0] % curses.LINES, pos[1] % curses.COLS)

    def is_food_eaten(self, *args: Tuple[int, int]) -> bool:
        head, food = args

        hy, hx = head
        fy, fx = food

        dx = hx - fx

        return hy == fy and 0 <= dx <= 3
        
        # return head == food


