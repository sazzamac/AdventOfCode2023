import re
import sys
from enum import Enum


class Colour(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'


valid_game = {Colour.RED.value: 12, Colour.GREEN.value: 13, Colour.BLUE.value: 14}


class Game:

    @
    def get_games(self, filename: str) -> str:
    file = open(filename, 'r')
    games = [line.replace('\n', '') for line in file]
    return games


def get_game_id(game_record: str) -> int:
    split_prefix = re.split(r'Game\s+', game_record)
    split_suffix = re.split(r':\s*.*', split_prefix[1])
    return int(split_suffix[0])


def get_game_sets(game_record: str) -> list:
    sets_str = re.split(r':\s+', game_record)[1]
    sets = re.split(r';\s+', sets_str)
    game_sets = list()
    for game_set in sets:
        game_set_dict = dict()
        cubes = re.split(r',\s*', game_set)
        for cube in cubes:
            chars = re.split(r'\s+', cube)
            game_set_dict[chars[1]] = int(chars[0])
        game_sets.append(game_set_dict)
    return game_sets


def is_set_valid(game_set: dict) -> bool:
    for drawn_colour, colour_count in game_set.items():
        if colour_count > valid_game[drawn_colour]:
            return False
    return True


def is_game_valid(game_record: str) -> bool:
    for game_set in get_game_sets(game_record):
        if not is_set_valid(game_set):
            return False
    return True


def get_sum_of_valid_game_ids(filename: str) -> int:
    games = get_games(filename)
    sum_of_valid_game_ids = 0
    for game_record in games:
        if is_game_valid(game_record):
            game_id = get_game_id(game_record)
            sum_of_valid_game_ids += game_id
    return sum_of_valid_game_ids


def get_min_cubes_to_make_game_possible(game_record: str) -> dict:
    min_num_cubes = {colour.value: 0 for colour in Colour}
    for game_set in get_game_sets(game_record):
        for drawn_colour, colour_count in game_set.items():
            assert drawn_colour in [colour.value for colour in Colour], f'{drawn_colour} colour not valid!'
            if min_num_cubes[drawn_colour] < colour_count:
                min_num_cubes[drawn_colour] = colour_count
    return min_num_cubes


def get_power_of_cube_set(game_set: dict):
    power = 1
    for colour_count in game_set.values():
        power = colour_count * power
    return power


if __name__ == '__main__':
    game_input = sys.argv[1]
    sum_of_valid_game_ids = get_sum_of_valid_game_ids(game_input)
    print(sum_of_valid_game_ids)

    sum_of_powers = 0
    for game_record in get_games(game_input):
        min_cubes_set = get_min_cubes_to_make_game_possible(game_record)
        sum_of_powers += get_power_of_cube_set(min_cubes_set)
    print(sum_of_powers)
