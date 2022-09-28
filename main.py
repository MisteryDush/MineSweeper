import random
from getkey import getkey, keys
import os
from shutil import get_terminal_size

ROWS = 8
COLS = 8
FIELD = []
CHANCE = 20
choice = 0
restart = True
lose = False
victory = False


def restart_game():
    global restart, lose, FIELD
    choice = input('Restart game? Y/n\n >> ')
    if choice.lower() == 'y':
        restart = True
        FIELD = []
    else:
        restart = False


def open_cell():
    global choice, lose
    cell = FIELD[choice]
    if cell.hide:
        cell.hide = False
        if cell.bomb:
            os.system('cls')
            get_field()
            lose = True
            print("""
                        __     __             _                  _   
                        \ \   / /            | |                | |  
                         \ \_/ /___   _   _  | |      ___   ___ | |_ 
                          \   // _ \ | | | | | |     / _ \ / __|| __|
                           | || (_) || |_| | | |____| (_) |\__ \| |_ 
                           |_| \___/  \__,_| |______|\___/ |___/ \__|
                           """)
            restart_game()


def is_victory():
    global victory
    b = 0
    flagged_tp = 0
    flagged_fn = 0
    f = FIELD
    for cell in f:
        if cell.bomb:
            b += 1
            if cell.flagged:
                flagged_tp += 1
        else:
            if cell.flagged:
                flagged_fn += 1
    if flagged_tp == b and flagged_fn == 0:
        victory = True
    else:
        victory = False


def flag_cell():
    global choice
    cell = FIELD[choice]
    if cell.hide:
        cell.flagged = True
    is_victory()


def input_handler(key):
    if key == "w":
        go_up()
    elif key == "s":
        go_down()
    elif key == "a":
        go_left()
    elif key == "d":
        go_right()
    elif key == keys.ENTER or key == keys.SPACE:
        open_cell()
    elif key == "f":
        flag_cell()
    elif key == keys.ESC:
        quit()


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
    global choice, columns, lines
    for row in range(ROWS):
        output = ''
        for col in range(COLS):
            cell = FIELD[col + row * COLS]
            if col + row * COLS == choice:
                if not cell.hide:
                    output += '|*|' if cell.bomb else f'|{cell.neighbours}|'
                elif cell.flagged:
                    output += '|F|'
                else:
                    output += '|#|'
            else:
                if not cell.hide:
                    output += ' * ' if cell.bomb else f' {cell.neighbours} '
                elif cell.flagged:
                    output += ' F '
                else:
                    output += ' # '
        print(output.center(columns))


def populate_field():
    for i in range((COLS * ROWS)):
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
                upper_cell_index = cell_index - COLS if cell_index - COLS >= 1 else 0
                lower_cell_index = ROWS * COLS if cell_index + COLS > len(FIELD) else cell_index + COLS
                if cell_index % COLS == 0:
                    try:
                        if cell_index >= COLS:
                            for i in range(0, 2):
                                if FIELD[upper_cell_index + i].bomb:
                                    cell.neighbours += 1
                        for i in range(0, 2):
                            if i == 0:
                                continue
                            elif FIELD[cell_index + i].bomb:
                                cell.neighbours += 1
                        if cell_index < len(FIELD) - COLS:
                            for i in range(0, 2):
                                if FIELD[lower_cell_index + i].bomb:
                                    cell.neighbours += 1
                    except:
                        pass
                elif cell_index % COLS == COLS - 1:
                    try:
                        if cell_index >= COLS:
                            for i in range(-1, 1):
                                if FIELD[upper_cell_index + i].bomb:
                                    cell.neighbours += 1
                        for i in range(-1, 1):
                            if i == 0:
                                continue
                            elif FIELD[cell_index + i].bomb:
                                cell.neighbours += 1
                        if cell_index < len(FIELD) - COLS:
                            for i in range(-1, 1):
                                if FIELD[lower_cell_index + i].bomb:
                                    cell.neighbours += 1
                    except:
                        pass
                else:
                    try:
                        if cell_index >= COLS:
                            for i in range(-1, 2):
                                if FIELD[upper_cell_index + i].bomb:
                                    cell.neighbours += 1
                        for i in range(-1, 2):
                            if i == 0:
                                continue
                            elif FIELD[cell_index + i].bomb:
                                cell.neighbours += 1
                        if cell_index < len(FIELD) - COLS:
                            for i in range(-1, 2):
                                if FIELD[lower_cell_index + i].bomb:
                                    cell.neighbours += 1
                    except:
                        pass


class Cell:
    def __init__(self, bomb=False):
        self.bomb = bomb
        self.neighbours = 0
        self.hide = True
        self.flagged = False


def print_name():
    print("""
      __  __   _                   _____                                                
     |  \/  | (_)                 / ____|                                               
     | \  / |  _   _ __     ___  | (___   __      __   ___    ___   _ __     ___   _ __ 
     | |\/| | | | | '_ \   / _ \  \___ \  \ \ /\ / /  / _ \  / _ \ | '_ \   / _ \ | '__|
     | |  | | | | | | | | |  __/  ____) |  \ V  V /  |  __/ |  __/ | |_) | |  __/ | |   
     |_|  |_| |_| |_| |_|  \___| |_____/    \_/\_/    \___|  \___| | .__/   \___| |_|   
                                                                   | |                  
                                                                   |_|                  
    """.center(columns))


def print_controls():
    print("""
    w - up
    s - down
    a - left
    d - right
    space/enter - open cell
    f - flag cell
    esc - exit""")


def display_win_message():
    os.system('cls')
    print("""
 __     __          __          __         
 \ \   / /          \ \        / /         
  \ \_/ /__  _   _   \ \  /\  / /__  _ __  
   \   / _ \| | | |   \ \/  \/ / _ \| '_ \ 
    | | (_) | |_| |    \  /\  / (_) | | | |
    |_|\___/ \__,_|     \/  \/ \___/|_| |_|
                                           
                                           
""")


def setting_up():
    global ROWS, COLS, CHANCE
    print('How many rows do you want? Default: 5')
    try:
        ROWS = int(input('>>> '))
        if ROWS > 25 or ROWS <= 0:
            ROWS = 5
    except ValueError:
        ROWS = 5
    print('How many columns do you want? Default: 5')
    try:
        COLS = int(input('>>> '))
        if COLS > 25 or COLS <= 0:
            COLS = 5
    except ValueError:
        COLS = 5
    print('Percentage of bombs on the field? Default: 30')
    try:
        CHANCE = int(input('>>> '))
        if CHANCE <= 0 or CHANCE >= 100:
            CHANCE = 30
    except ValueError:
        CHANCE = 30


while True:
    os.system('cls')
    setting_up()
    populate_field()
    get_neighbouring_bombs()
    columns = get_terminal_size().columns
    lines = get_terminal_size().lines
    while True:
        print_name()
        print_controls()
        get_field()
        key = getkey()
        input_handler(key)
        if victory:
            display_win_message()
            restart_game()
            break
        else:
            os.system('cls')
            if lose:
                break
    if not restart:
        break
    victory = False
    lose = False

"""
                              `-:/+++++++/++:-.                                          
                            .odNMMMMMMMMMMMMMNmdo-`                                      
                           +mMMNmdhhhhhhhhhdmNMMMNd/`                                    
                          sMMMmhyyyyyyyyyyyyyyhmNMMMh-                                   
                         +MMMdyyyyyyyhhhhdddddddmMMMMN/                                  
                        `NMMmyyyyyymNNMMNNNmmmmmmmNNMMMy`                                
                        :MMMhyyyyyNMMMho+//:-.....-:omMMd-                               
                    ```:mMMNhyyyyhMMMh+::::-        `:sNMN:                              
                 -oyhdmMMMMmhyyyyhMMNyy+::::---------::yMMm                              
                +MMMMNNNMMMdhyyyyhMMNyyyso/::::::://+oshMMM`                             
                NMMNhyyyMMMhhyyyyyNMMmyyyyyyssssyyyyyyymMMd                              
                MMMdyyyhMMNhhyyyyyhNMMNdyyyyyyyyyyyhdmMMMN-                              
                MMMdhhhdMMNhhhyyyyyymMMMMNmmmmmmNNMMMMMMN.                               
                MMMhhhhdMMNhhhyyyyyyyhdmNNNMMNNNmmdhhdMMd                                
               `MMMhhhhdMMNhhhhyyyyyyyyyyyyyyyyyyyyyydMMM.                               
               .MMMhhhhdMMNhhhhyyyyyyyyyyyyyyyyyyyyyydMMM:                               
               .MMNhhhhdMMNhhhhhyyyyyyyyyyyyyyyyyyyyhhMMM+                               
               -MMNhhhhdMMNhhhhhyyyyyyyyyyyyyyyyyyyyhdMMM/                               
               -MMMhhhhdMMNhhhhhhhyyyyyyyyyyyyyyyyyhhdMMM-                               
               `MMMhhhhhMMNhhhhhhhhhhyyyyyyyyyyyhhhhhmMMN                                
                hMMmhhhhMMNhhhhhhhhhhhhhhhhhhhhhhhhhhNMMy                                
                :MMMNmddMMMhhhhhhhhhhddddhhhhhhhhhhhdMMM/                                
                 :hNMMMMMMMdhhhhhhhhdMMMMMMNNNNNdhhhNMMN`                                
                   .-/+oMMMmhhhhhhhhmMMmyhMMMddhhhhdMMMy                                 
                        hMMNhhhhhhhhmMMd :MMMhhhhhhdMMM+                                 
                        sMMNhhhhhhhhNMMm .MMMdhhhhhdMMN.                                 
                        /MMMdhhhhhhdMMM+  oNMMNNNNNMMm:                                  
                        `dMMMNmmmNNMMMh`   -syyyyhhy/`                                   
                         `/hmNNNNNmdh/`                                                  
                            `.---..`
"""
