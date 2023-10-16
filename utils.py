import uuid

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

    if (abs(number) < 0.0001):
        return str(round(number, 6))

    num_str = str(number)

    if '.' not in num_str:
        return str(number)
    else:
        integer_part, decimal_part = num_str.split('.')
        integer_len = len(integer_part)

        decimal_presicion = 5 - integer_len if integer_len < 3 else 1

        integer_str = '{:,}'.format(int(integer_part))
        returnStr = f'{integer_str}.{decimal_part[0:decimal_presicion]}'

    return returnStr