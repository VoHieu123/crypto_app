import uuid
from PyQt6.QtCore import pyqtSignal, QObject
import subprocess

def resynch():
    try:
        subprocess.run(['w32tm', '/resync'], check=True)
    except:
        # print("Synchronize failed!")
        pass

class Communication(QObject):
    ui_signal = pyqtSignal()

class Range:
    def __init__(self, start: float, end: float):
        if start > end and start != -1 and end!= -1:
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

def auto_format(text, color="black", background_color=None, format_number=None, font_weight="normal", font_size=14):

    def text_format(text, color, background_color, font_weight, font_size):
        return f"<span style='font-size: {font_size}pt; background-color: {background_color}; font-weight: {font_weight}; color: {color};'>{text}</span>" if background_color else \
               f"<span style='font-size: {font_size}pt; color: {color}; font-weight: {font_weight};'>{text}</span>"

    def number_format(number, format_number):
        if format_number is None:
            if (abs(number) < 0.0001):
                return str(round(number, 6))

            integer_part, decimal_part = (str(number)).split('.')
            integer_len = len(integer_part)
            integer_str = '{:,}'.format(int(integer_part))

            returnStr = integer_str if integer_len >= 4 else f'{integer_str}.{decimal_part[0:(5 - integer_len)]}'

        else:
            returnStr = f"{number:{format_number}}"

        return returnStr

    try:
        text = number_format(float(text), format_number=format_number)
    except:
        pass

    return text_format(text, color=color, background_color=background_color, font_weight=font_weight, font_size=font_size)