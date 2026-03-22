import curses
from math import ceil
from typing import List, Tuple
from tetris.shape import Shape
from random import  choice, shuffle
from consts import BLOCK, hide_cursor
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

    @hide_cursor() # type: ignore
    def start(self) -> None:
        shuffle(self.shapes)
        self.init_waiting_list()
        shape: Shape = self.waiting_list.pop()
        while self.is_running:
            shape.fall()
            if shape.is_grounded:
                shape.reset()
                self.shapes.append(shape)
                self.lock.acquire()
                self.waiting_list.append(
                        self.shapes.pop(0))
                self.lock.release()
                shape = self.waiting_list.pop(0)

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

    def strip_lines(self) -> None:
        raise NotImplementedError()

            



