import uuid
from decimal import Decimal, ROUND_HALF_UP

def round_to_auto_decimal_places(number):
    decimal_number = Decimal(str(number))
    return decimal_number.quantize(Decimal('1.000'))

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

def auto_format(number):
    num_str = str(number)

    if '.' in num_str:
        integer_part, decimal_part = num_str.split('.')
        integer_len = len(integer_part)
    else:
        integer_len = 0

    if (abs(number) > 0.0001):
        returnStr = str(round(number, 5 - integer_len if integer_len < 3 else None))
    else:
        returnStr = str(round(number, 5))

    return returnStr