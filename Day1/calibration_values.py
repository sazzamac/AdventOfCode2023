import sys
from typing import Iterable, Union


class Calibration:

    def __init__(self):
        pass

    @staticmethod
    def get_lines(filename: str) -> str:
        file = open(filename, 'r')
        lines = [line.replace('\n', '') for line in file]
        return lines

    @classmethod
    def get_first_int_char(cls, line: Iterable) -> Union[str, None]:
        for char in line:
            try:
                int(char)
                return char
            except ValueError:
                pass
        return None

    @classmethod
    def get_calibration_value(cls, line: Iterable) -> int:
        first_digit = cls.get_first_int_char(line)
        last_digit = cls.get_first_int_char(line[::-1])
        calibration_str = first_digit + last_digit
        calibration_value = int(calibration_str)
        if not isinstance(calibration_value, int):
            raise TypeError
        return calibration_value

    @classmethod
    def sum_calibration_values(cls, calibration_values: list) -> int:
        summed_value = 0
        for calibration_value in calibration_values:
            summed_value += calibration_value
        return summed_value


if __name__ == '__main__':
    streamable_file = sys.argv[1]
    lines = Calibration.get_lines(streamable_file)
    calibration_values = [Calibration.get_calibration_value(line) for line in lines]
    sum_of_calibration_values = Calibration.sum_calibration_values(calibration_values)
    print(sum_of_calibration_values)



