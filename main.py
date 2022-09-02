import random
from getkey import getkey, keys

ROWS = 4
COLS = 8
FIELD = []
CHANCE = 10
choice = 0


def input_handler(key):
    if key == "w":
        go_up()
    elif key == "s":
        go_down()
    elif key == "a":
        go_left()
    elif key == "d":
        go_right()


def go_up():
    global choice
    if choice > COLS - 1:
        choice -= COLS


def go_down():
    global choice
    if choice < COLS * ROWS - COLS:
        choice += COLS


def go_left():
    global choice
    if choice != 0:
        choice -= 1


def go_right():
    global choice
    if choice != ROWS * COLS - 1:
        choice += 1


def get_field():
    global choice
    for row in range(ROWS):
        for col in range(COLS):
            cell = FIELD[col + row * COLS]
            if col + row * COLS == choice:
                if not cell.hide:
                    print('|*|' if cell.bomb else f'|{cell.neighbours}|', end='')
                else:
                    print('|#|', end='')
            else:
                if not cell.hide:
                    print(' * ' if cell.bomb else f' {cell.neighbours} ', end='')
                else:
                    print(' # ', end='')
        print()


def populate_field():
    for i in range((COLS * ROWS + 1)):
        rint = random.randint(1, 100)
        if rint < CHANCE:
            cell = Cell(bomb=True)
        else:
            cell = Cell()
        FIELD.append(cell)


def get_neighbouring_bombs():
    for row in range(ROWS):
        for col in range(COLS):
            cell = FIELD[col + row * COLS]
            if not cell.bomb:
                cell_index = FIELD.index(cell)
                upper_cell_index = cell_index - 8 if cell_index - 8 > 1 else 0
                lower_cell_index = ROWS * COLS if cell_index + 8 > len(FIELD) else cell_index + 8
                if cell_index % COLS == 0:
                    try:
                        if upper_cell_index > 2:
                            for i in range(0, 2):
                                if FIELD[upper_cell_index + i].bomb:
                                    cell.neighbours += 1
                        for i in range(0, 2):
                            if i == 0:
                                continue
                            elif FIELD[cell_index + i].bomb:
                                cell.neighbours += 1
                        for i in range(0, 2):
                            if FIELD[lower_cell_index + i].bomb:
                                cell.neighbours += 1
                    except:
                        pass
                elif cell_index % COLS == COLS - 1:
                    try:
                        if upper_cell_index > 2:
                            for i in range(-1, 1):
                                if FIELD[upper_cell_index + i].bomb:
                                    cell.neighbours += 1
                        for i in range(-1, 1):
                            if i == 0:
                                continue
                            elif FIELD[cell_index + i].bomb:
                                cell.neighbours += 1
                        for i in range(-1, 1):
                            if FIELD[lower_cell_index + i].bomb:
                                cell.neighbours += 1
                    except:
                        pass
                else:
                    try:
                        if upper_cell_index > 2:
                            for i in range(-1, 2):
                                if FIELD[upper_cell_index + i].bomb:
                                    cell.neighbours += 1
                        for i in range(-1, 2):
                            if i == 0:
                                continue
                            elif FIELD[cell_index + i].bomb:
                                cell.neighbours += 1
                        for i in range(-1, 2):
                            if FIELD[lower_cell_index + i].bomb:
                                cell.neighbours += 1
                    except:
                        pass


class Cell:
    def __init__(self, bomb=False):
        self.bomb = bomb
        self.neighbours = 0
        self.hide = False


populate_field()
get_neighbouring_bombs()
while True:
    get_field()
    key = getkey()
    input_handler(key)
