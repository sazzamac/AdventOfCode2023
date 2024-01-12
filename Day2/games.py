import re
import sys


valid_game = dict(red=12, green=13, blue=14)


def get_lines(filename: str) -> str:
        file = open(filename, 'r')
        lines = [line.replace('\n', '') for line in file]
        return lines


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
    games = get_lines(filename)
    sum_of_valid_game_ids = 0
    for game_record in games:
        if is_game_valid(game_record):
            game_id = get_game_id(game_record)
            sum_of_valid_game_ids += game_id
    return sum_of_valid_game_ids


if __name__ == '__main__':
    game_input = sys.argv[1]
    sum_of_valid_game_ids = get_sum_of_valid_game_ids(game_input)
    print(sum_of_valid_game_ids)
