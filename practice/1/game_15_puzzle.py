import random

EMPTY_MARK = 'x'

MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1,
}


def shuffle_field(gameMap):
    mixingDepth = random.randint(50, 100)
    for i in range(mixingDepth):
        key = random.choice(["w", "s", "d", "a"])
        perform_move(gameMap, key)
    return gameMap
    pass


def print_field(gameMap):
    for i in range(len(gameMap)):
        if i % 4 == 0 and i != 0:
            print()
        print(gameMap[i], end=' ')
    pass


def is_game_finished(gameMap):
    if gameMap[:len(gameMap) - 1] == [(i + 1) for i in range(15)]:
        return True
    else:
        return False
    pass


def perform_move(gameMap, key):
    indexEmptyTile = gameMap.index('x')

    if key == 'w':
        if indexEmptyTile in [12, 13, 14, 15]:
            return None
        else:
            gameMap[indexEmptyTile], gameMap[indexEmptyTile + 4] = gameMap[indexEmptyTile + 4],  gameMap[indexEmptyTile]

    elif key == 's':
        if indexEmptyTile in [0, 1, 2, 3]:
            return None
        else:
            gameMap[indexEmptyTile], gameMap[indexEmptyTile - 4] = gameMap[indexEmptyTile - 4],  gameMap[indexEmptyTile]

    elif key == 'a':
        if indexEmptyTile in [3, 7, 11, 15]:
            return None
        else:
            gameMap[indexEmptyTile], gameMap[indexEmptyTile + 1] = gameMap[indexEmptyTile + 1],  gameMap[indexEmptyTile]
    else:
        if indexEmptyTile in [0, 4, 8, 12]:
            return None
        else:
            gameMap[indexEmptyTile], gameMap[indexEmptyTile - 1] = gameMap[indexEmptyTile - 1], gameMap[indexEmptyTile]
    pass


def handle_user_input():
    print()
    key = input()
    return key

    pass


def main():
    GameMap = shuffle_field([(i + 1) for i in range(15)] + [EMPTY_MARK])

    while not(is_game_finished(GameMap)):
        print_field(GameMap)
        perform_move(GameMap, handle_user_input())
    print("WIN")

    pass


if __name__ == '__main__':

    main()


