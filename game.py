# -*- coding: utf-8 -*-

# `random` module is used to shuffle field, see§:
# https://docs.python.org/3/library/random.html#random.shuffle
import random


# Empty tile, there's only one empty cell on a field:
EMPTY_MARK = ' x'

# Dictionary of possible moves if a form of: 
# key -> delta to move the empty tile on a field.
MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1,
}


def shuffle_field():
    field = [
        ' 1', ' 2', ' 3', ' 4',
        ' 5', ' 6', ' 7', ' 8',
        ' 9', '10', '11', '12',
        '13', '14', '15', EMPTY_MARK
    ]
    m = 1
    n = 0
    e = 0
    random.shuffle(field)
    while (n + e) % 2 != 0:
        for i in range(len(field)):
            if (i + m) > 15:
                m = 15 - i
            if field[i] > field[i + m]:
                m += 1
                n += 1
            elif field[i] < field[i + m]:
                m += 1
            elif field[i] < field[i + m]:
                e = field.index(' x')
        if (n + e) % 2 == 1:
            random.shuffle(field)
    return field


def print_field(field):
    print(field[0] + '   ' + field[1] + '   ' + field[2] + '   ' + field[3]+'\n'+
          field[4] + '   ' + field[5] + '   ' + field[6] + '   ' + field[7]+'\n'+
          field[8] + '   ' + field[9] + '   ' + field[10] + '   ' + field[11]+'\n'+
          field[12] + '   ' + field[13] + '   ' + field[14] + '   ' + field[15])


def is_game_finished(field):
    """
    This method checks if the game is finished.
    :param field: current field state.
    :return: True if the game is finished, False otherwise.
    """
    pass


def perform_move(field, key):
    pos = field.index(EMPTY_MARK)
    print(pos)
    print(MOVES.get(key))
    if key == 'd':
        if pos == 3 or pos == 7 or pos == 11 or pos == 15:
            print('Wrong move!')
        elif pos >=0 and pos < 3 or pos >=4 and pos < 7 or pos >=8 and pos < 11 or pos >=12 and pos < 15:
            field.insert(pos + MOVES.get(key), field.pop(pos))
        pos += MOVES.get(key)
    elif key == 'a':
        if pos == 0 or pos == 4 or pos == 8 or pos == 12:
            print('Wrong move!')
        elif pos >0 and pos <= 3 or pos >4 and pos <= 7 or pos >8 and pos <= 11 or pos >12 and pos <= 15:
            field.insert(pos + MOVES.get(key), field.pop(pos))
            pos += MOVES.get(key)
    elif key == 'w':
        if pos == 0 or pos == 1 or pos == 2 or pos == 3:
            print('Wrong move!')
        elif pos >3 and pos <= 15:
            field.insert(pos + MOVES.get(key), field.pop(pos))
            pos += MOVES.get(key)
            field.insert(pos - MOVES.get(key), field.pop(pos + 1))
    elif key == 's':
        if pos == 12 or pos == 13 or pos == 14 or pos == 15:
            print('Wrong move!')
        elif pos >= 0 and pos < 12:
            field.insert(pos + MOVES.get(key), field.pop(pos))
            pos += MOVES.get(key)
            field.insert(pos - MOVES.get(key), field.pop(pos - 1))
    print(pos)
    """
    Moves empty-tile inside the field.
    :param field: current field state.
    :param key: move direction.
    :return: new field state (after the move).
    :raises: IndexError if the move can't me done.
    """
    pass


def handle_user_input():
    key = input()
    if key in MOVES.keys():
        pass
    else:
        print('Wrong key!')
    return key


def main():
    field = shuffle_field()
    print_field(field)
    while True:
        key = handle_user_input()
        perform_move(field, key)
        print_field(field)


if __name__ == '__main__':
    # See what this means:
    # http://stackoverflow.com/questions/419163/what-does-if-name-main-do

    main()
