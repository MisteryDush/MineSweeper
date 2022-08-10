import random

HEIGHT = 4
WIDTH = 8
FIELD = []
CHANCE = 30


def main():
    populate_field()
    get_field()


def get_field():
    for row in range(HEIGHT):
        for col in range(WIDTH):
            print('*' if FIELD[col + row * WIDTH].bomb else '#', end='')
        print()


def populate_field():
    for i in range((WIDTH * HEIGHT + 1)):
        rint = random.randint(1, 100)
        if rint < CHANCE:
            cell = Cell(bomb=True)
        else:
            cell = Cell()
        FIELD.append(cell)


def get_neighbouring_bombs():
    pass

class Cell:
    def __init__(self, bomb=False):
        self.bomb = bomb


if __name__ == '__main__':
    main()
