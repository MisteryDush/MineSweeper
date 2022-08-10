HEIGHT = 4
WIDTH = 8
FIELD = []


def main():
    populate_field()
    len(FIELD)
    get_field()


def get_field():
    for i in range(HEIGHT):
        print(''.join(FIELD[(0 + WIDTH * i):(WIDTH + WIDTH * i + 1)]))


def populate_field():
    for i in range((WIDTH * HEIGHT + 1)):
        FIELD.append('#')


class Cell:
    def __init__(self, bomb=False):
        self.bomb = bomb


if __name__ == '__main__':
    main()
