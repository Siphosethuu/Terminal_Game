import curses
from math import ceil
from typing import List, Tuple
from tetris.shape import Shape, Action
from tetris.utils import TOP_LEFT_CORNER, BOTTOM_RIGHT_CORNER
from random import  choice, shuffle
from consts import BLOCK, LINES, hide_cursor, draw_square_boundary
from threading import Lock, Thread

shapes: List[str] = ['L', 'J', 'Z', 'S', 'T', 'O']
class Game:
    def __init__(self, screen: curses.window) -> None:
        self.screen = screen
        self.shapes: List[Shape] = Shape.create_shapes(self.screen)
        self.lock: Lock = Lock()
        self.score: int = 0
        self.is_running: bool = True
        self.screen.nodelay(True)
        self.screen.keypad(True)
        bkgd_info: int = self.screen.getbkgd() # type: ignore
        self.bkgd_attr = bkgd_info & curses.A_ATTRIBUTES
        self.bkgd_char = chr( bkgd_info & curses.A_CHARTEXT )
        self.top, self.left = TOP_LEFT_CORNER
        self.bottom, self.right = BOTTOM_RIGHT_CORNER


    @hide_cursor
    def start(self) -> None:
        shuffle(self.shapes)
        self.init_waiting_list()
        shape: Shape = self.waiting_list.pop()
        shape.falling_effect.activate()
        self.draw_waiting_list_display_bounds()
        self.draw_game_bounds()
        self.update_waiting_list_display()
        while self.is_running:
            if shape.is_grounded:
                self.screen.addstr(0, 0, f"Shape({shape.shape}) is grounded".center(LINES), curses.A_BOLD | curses.A_STANDOUT)
                if shape.y == self.top:
                    self.screen.addstr(15, 15, f"GAME OVER", curses.A_BOLD | curses.A_STANDOUT)
                    self.screen.refresh()
                    curses.napms(6000)
                    break
                # self.strip_lines(shape)
                shape.reset()
                self.shapes.append(shape)
                self.lock.acquire()
                self.waiting_list.append(
                        self.shapes.pop(0))
                self.lock.release()
                shape = self.waiting_list.pop(0)
                shape.falling_effect.activate()
                self.update_waiting_list_display()

            shape.input()

    def init_waiting_list(self) -> None:
        self.waiting_list: List[Shape] = []
        self.lock.acquire()
        for _ in range(0, 3):
            self.waiting_list.append(
                self.shapes.pop(0))
        self.lock.release()
        

    def permanent_shuffler(self) -> None:
        while self.is_running:
            self.lock.acquire()
            shuffle(self.shapes)
            self.lock.release()

    def strip_lines(self, shape: Shape) -> None:
        lowest_y, _ = max(shape.body, key=lambda pos: pos[0])
        top_y, _ = min(shape.body, key=lambda pos: pos[0])
        lowest_y += shape.y
        top_y += shape.y

        lines_cleared: int = 0
        for line in range(lowest_y, top_y - 1, -1):
            for x in range(self.left, self.right):
                char_info = self.screen.inch(line, x)
                char_attr = char_info & curses.A_ATTRIBUTES
                if char_attr == self.bkgd_attr:
                    break
            else:
                self.clear_line(line, self.left, self.right)
                lines_cleared += 1
    

    def clear_line(self, line: int, start: int, end: int) -> None:
        if line == self.top:
            return
        for x in range(start, end, 1):
            self.screen.addstr(
                line, x, ' ', self.bkgd_attr
            )

    def lower_shapes(self) -> None:
        raise NotImplementedError

    def draw_game_bounds(self) -> None:
        draw_square_boundary(self.screen, self.top, self.left, self.bottom, self.right)

    def draw_waiting_list_display_bounds(self) -> None:
        self.waiting_list_left = self.right + 5
        self.waiting_list_top = self.top + 2
        self.waiting_list_bottom = self.top + 15
        self.waiting_list_right = self.waiting_list_left + 10

        draw_square_boundary(self.screen, 
            self.waiting_list_top, self.waiting_list_left,
            self.waiting_list_bottom, self.waiting_list_right)

    
    def update_waiting_list_display(self) -> None:
        if len(self.waiting_list) > 3:
            raise ValueError("First remove one item.")

        for line in range(self.waiting_list_top, self.waiting_list_bottom):
            self.clear_line(line, self.waiting_list_left, self.waiting_list_right)

        for index, shape in enumerate(self.waiting_list):
            shape.display(Action.DRAW, (self.waiting_list_top + (index * 2) + 2, self.waiting_list_left + 4))
        




