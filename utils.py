import uuid
from PyQt6.QtCore import pyqtSignal, QObject

class Communication(QObject):
    ui_signal = pyqtSignal()

class Range:
    def __init__(self, start: float, end: float):
        if start > end:
            exit("Range object error.")
        self.start = start
        self.end = end

    def __eq__(self, __value: object) -> bool:
        return self.start == __value.start and self.end == __value.end

    def out_of_range(self, number) -> bool:
        return number < self.start or number > self.end

def change_last_letter(word, new_letter):
        if len(word) < 1:
            return word

        word_list = list(word)
        word_list[-1] = new_letter
        modified_word = ''.join(word_list)

        return modified_word

def substring_after(s, delim):
    return s.partition(delim)[2]

def substring_before(s, delim):
    return s.partition(delim)[0]

def convert_to_float(data):
    if isinstance(data, dict):
        return {key: convert_to_float(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [convert_to_float(item) for item in data]
    elif isinstance(data, str):
        try:
            return 0 if data == "" else float(data)
        except ValueError:
            return data
    else:
        return data

def generate_uuid():
    return str(uuid.uuid4())

def auto_format(number, color=None):

    number = float(number)

    if (abs(number) < 0.0001):
        return f"<font color='{color}'>{str(round(number, 5))}</font>" if color else str(round(number, 5))

    integer_part, decimal_part = (str(number)).split('.')
    integer_len = len(integer_part)
    integer_str = '{:,}'.format(int(integer_part))

    returnStr = integer_str if integer_len >= 4 else f'{integer_str}.{decimal_part[0:(5 - integer_len)]}'

    if color:
        returnStr = f"<font color='{color}'>{returnStr}</font>"

    return returnStr