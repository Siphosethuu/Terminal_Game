"""
    Author:
        clear_code_projects (YouTuber)
"""

from time import sleep 
import threading

class Timer:
    def __init__(self, interval: float, func) -> None:
        self.interval: float = interval
        self.active: bool = False
        self.thread = threading.Thread(target=self.run)
        self.thread.daemon = True
        self.function = func

    def activate(self) -> None:
        self.active = True
        self.thread.start()

    def deactivate(self) -> None:
        self.active = False

    def run(self) -> None:
        while self.active:
            sleep(self.interval)
            self.function()

