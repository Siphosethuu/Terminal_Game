import curses


from consts import LINES, COLS

from snake.stage import Stage
    
BODY_PART: str = '  '
SNAKE_FOOD: str = ' @'



class Keys:
    UP: int = curses.KEY_UP
    ESC: int = 27
    DOWN: int = curses.KEY_DOWN
    LEFT: int = curses.KEY_LEFT
    RIGHT: int = curses.KEY_RIGHT



def get_box_stage() -> Stage:
    walls = {}
    for y in range(1, LINES):
        walls[(y, 0)] = ' '
        walls[(y, 1)] = ' '
        walls[(y, COLS - 1)] = ' '
        walls[(y, COLS - 2)] = ' '
        walls[(y, COLS - 3)] = ''


    for x in range(0, COLS + 1):
        walls[(1, x)] = ' '
        walls[(LINES, x)] = ' '

    return Stage(walls)


def get_tunnel_stage() -> Stage:
    walls = {}
    def get_conners(*args: int) -> None:
        start_y, start_x, LENGTH = args

        for y in range(start_y, start_y + LENGTH):
            walls[(y, 0)] = ' '
            walls[(y, 1)] = ' '

            walls[(y, COLS - 1)] = '  '
            walls[(y, COLS - 2)] = '    '
            walls[(y, COLS - 3)] = ''


        for x in range(start_x, start_x + LENGTH):
            walls[(1, x)] = ' '
            walls[(LINES, x)] = ' '

    LENGTH: int = COLS # min(LINES // 4, COLS // 4)

    get_conners(0, 0, LENGTH)

    get_conners(LINES - LENGTH, COLS - LENGTH, LENGTH)

    CENTER_Y1: int = (LINES - LENGTH) // 2
    CENTER_Y2: int = (LINES + LENGTH) // 2 

    for x in range(LENGTH, COLS - LENGTH):
        walls[(CENTER_Y2, x)] = ' '
        walls[(CENTER_Y1, x)] = ' '

    return Stage(walls)


def get_half_world_stage() -> Stage:
    CENTER_Y: int = LINES + 1 // 4
    wall = {(CENTER_Y, x): ' ' for x in range(0, COLS)}

    return Stage(wall)

def get_quarter_world_stage() -> Stage:
    raise NotImplementedError

