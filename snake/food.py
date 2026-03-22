from snake.snake import Snake
from snake.stage import Stage
from consts import LINES, COLS
from typing import List, Tuple
from random import choice


class Food:
    lines: List[int] = []
    cols : List[int] = []


    @staticmethod
    def set_valid_ranges( snake: Snake ) -> None:
        _, X = snake.get_head()
        Food.lines = [y for y in range(0, LINES - 1)]

        start: int = 0 if X % 2 == 0 else 1
        Food.cols = [x for x in range(start, COLS, 2)]



    @staticmethod
    def food(snake: Snake, stage: Stage) -> Tuple:
        """
            Returns a position that is not occupied by either the snake body or stage walls.
            Args:
                snake (Snake): snake object.
                stake (Stage): stage object.
            Returns:
                Tuple of two integers (y, x).
        """
        while True:
            y: int = choice( Food.lines )
            x: int = choice( Food.cols  )
            f = (y, x)
            if snake.overlaps(f):
                continue
            if stage.overlaps(f):
                continue
            
            return f


    @staticmethod
    def is_food_eaten(head, food) -> bool:
        """
            Given a head and food, checks if the food is is_food_eaten.
            Args:
                head (Tuple[int, int]): position of the head of the snake.
                food (Tuple[int, int]): position of the food.
            Returns:
                True if food is eaten else False.
        """
        hy, hx = head
        fy, fx = food
        return hy == fy and hx == fx


