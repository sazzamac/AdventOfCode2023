import sys


class Calibration:

    class CalibrationError:
        raise Exception

    @staticmethod
    def get_lines(file: BytesIO) -> str:
        lines = [line.append('') for line in file]
        return lines

    @classmethod
    def get_calibration_value(cls, line: str) -> int:
        int_chars = [int(char) for char in line]
        for int_char in enumerate(idx, int_chars):
            if int_char is not null:
                first_digit = line[idx]
            else:
                raise CalibrationError
        for int_char in enumerate(idx, int_chars[:-1]):
            if int_char is not null:
                last_digit = line[idx]
            else:
                raise CalibrationError
        calibration_str = first_digit + last_digit
        calibration_value = int(calibration_str)

        if not isinstance(calibration_value, int):
            raise CalibrationError
        return calibration_value

    @classmethod
    def sum_calibration_values(cls, calibration_values: Iterable) -> int:
        summed_value = 0
        for calibration_value in calibration_values:
            summed_value += calibration_value
        return summed_value


if __name__ == '__main__':
    streamable_file = sys.argv[0]
    lines = Calibration.get_lines(streamable_file)
    calibration_values = [Calibration.get_calibration_value(line) for line in lines]
    sum_of_calibration_values = Calibration.sum_calibration_values(calibration_values)
    print(sum_of_calibration_values)



