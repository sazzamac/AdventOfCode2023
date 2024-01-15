import re
import sys
from enum import Enum


class Colour(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'


class Game:
    valid_game = {Colour.RED.value: 12, Colour.GREEN.value: 13, Colour.BLUE.value: 14}

    def __init__(self, game_record: str):
        self.game = game_record

    def get_game_id(self) -> int:
        split_prefix = re.split(r'Game\s+', self.game)
        split_suffix = re.split(r':\s*.*', split_prefix[1])
        return int(split_suffix[0])

    def get_game_sets(self) -> list:
        sets_str = re.split(r':\s+', self.game)[1]
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

    @classmethod
    def is_set_valid(cls, game_set: dict) -> bool:
        for drawn_colour, colour_count in game_set.items():
            if colour_count > cls.valid_game[drawn_colour]:
                return False
        return True

    def is_game_valid(self) -> bool:
        for game_set in self.get_game_sets():
            if not self.is_set_valid(game_set):
                return False
        return True

    def get_min_cubes_to_make_game_possible(self) -> dict:
        min_num_cubes = {colour.value: 0 for colour in Colour}
        for game_set in self.get_game_sets():
            for drawn_colour, colour_count in game_set.items():
                assert drawn_colour in [colour.value for colour in Colour], f'{drawn_colour} colour not valid!'
                if min_num_cubes[drawn_colour] < colour_count:
                    min_num_cubes[drawn_colour] = colour_count
        return min_num_cubes

    @staticmethod
    def get_power_of_cube_set(game_set: dict) -> int:
        power = 1
        for colour_count in game_set.values():
            power = colour_count * power
        return power


if __name__ == '__main__':

    def get_game_records(filename) -> str:
        file = open(filename, 'r')
        games = [line.replace('\n', '') for line in file]
        return games


    filename = sys.argv[1]
    sum_of_valid_game_ids = 0
    sum_of_powers = 0

    for game_record in get_game_records(filename):
        game = Game(game_record)
        if game.is_game_valid():
            game_id = game.get_game_id()
            sum_of_valid_game_ids += game_id
        min_cubes_set = game.get_min_cubes_to_make_game_possible()
        sum_of_powers += Game.get_power_of_cube_set(min_cubes_set)
    print(f'Sum of valid game IDs: {sum_of_valid_game_ids}')
    print(f'Sum of powers: {sum_of_powers}')
