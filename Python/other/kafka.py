def go_north(position):
    i, j = position
    return (i, j + 1)


def go_east(position):
    i, j = position
    return (i + 1, j)


def go_south(position):
    i, j = position
    return (i, j - 1)


def go_west(position):
    i, j = position
    return (i - 1, j)


def look(position):
    return position


def quit_game(position):
    return None


def labyrinth(position, alive):
    print('You\'re in a maze of twisty passages, all alike.')
    return position, alive


def dark_forest(position, alive):
    print('You on a road in a dark forest. To the North you can see a tower.')
    return position, alive


def tall_tower(position, alive):
    print('There\'s a tall tower here, with no obvious door. A part leads east.')
    return position, alive


def rabbit_hole(position, alive):
    print('You fall down a rabbit hole into a labyrinth.')
    return (0, 0), alive


def lava_pit(position, alive):
    print('You fall into a lava pit :-(')
    return position, False


def play():
    position = (0, 0)
    alive = True

    while position:

        locations = {
            (0, 0): lambda: labyrinth,
            (1, 0): lambda: dark_forest,
            (1, 1): lambda: tall_tower,
            (2, 1): lambda: rabbit_hole,
            (3, 0): lambda: lava_pit
        }

        try:
            locations[position]
        except KeyError:
            print('There\'s nothing to here.')
        else:
            position, alive = locations[position]()(position, alive)

        if not alive:
            print('You\'re dead!')
            break

        # if position == (0, 0):
        #     print('You\'re in a maze of twisty passages, all alike.')
        # elif position == (1, 0):
        #     print('You on a road in a dark forest. To the North you can see a tower.')
        # elif position == (1, 1):
        #     print('There\'s a tall tower here, with no obvious door. A part leads east.')
        # else:
        #     print('There\'s nothing to here.')

        command = input()

        actions = {
            'N': go_north,
            'E': go_east,
            'S': go_south,
            'W': go_west,
            'L': look,
            'Q': quit_game
        }

        try:
            actions[command]
        except KeyError:
            print('I don\'t understand.')
        else:
            position = actions[command](position)

        # i, j = position
        #
        # if command == 'N':
        #     position = (i, j + 1)
        # elif command == 'E':
        #     position = (i + 1, j)
        # elif command == 'S':
        #     position = (i, j - 1)
        # elif command == 'W':
        #     position = (i - 1, j)
        # elif command == 'L':
        #     pass
        # elif command == 'Q':
        #     position = None
        # else:
        #     print('I don\'t understand.')

    else:  # no-break
        print('You\'ve chosen to leave the game.')


    print('Game over!')


if __name__ == '__main__':
    play()
