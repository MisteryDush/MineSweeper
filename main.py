import math
import random

ROWS = 4
COLS = 8
FIELD = []
CHANCE = 30


def main():
    populate_field()
    get_field()
    get_neighbouring_bombs()
    print()
    get_field()


def get_field():
    for row in range(ROWS):
        for col in range(COLS):
            cell = FIELD[col + row * COLS]
            print('*' if cell.bomb else f'{cell.neighbours}', end='')
            print('|', end='')
        print()
        print('-' * COLS * 2)


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


if __name__ == '__main__':
    main()
