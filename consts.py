


from os import get_terminal_size 

SIZE = get_terminal_size()
COLS: int = SIZE.columns - 1
LINES: int = SIZE.lines - 1
LINES_WRAP: int = LINES
COLS_WRAP:  int = COLS
