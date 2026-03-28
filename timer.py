"""
    Author:
        clear_code_projects (YouTuber)
"""

import time

class Timer:
    def __init__(self, interval: float, func) -> None:
        self.interval: float = interval
        self.start_time: float = 0
        self.active: bool = False
        self.function = func

    def start(self) -> None:
        self.active = True
        self.start_time = time.time()


    def stop(self) -> None:
        self.active = False
        self.start_time = 0

    
    def update(self, *args, **kwargs) -> None:
        elapsed: float = time.time() - self.start_time
        if elapsed >= self.interval:
            self.function(*args, **kwargs)

