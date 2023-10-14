import ntplib
from datetime import datetime
import uuid
import const
import time

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

def synchronize_time():
    ntp_server = 'pool.ntp.org'  # Use a reliable NTP server

    client = ntplib.NTPClient()

    retries_count = -1
    while True:
        retries_count += 1
        try:
            response = client.request(ntp_server)
            # Update the system time with the NTP server's time
            datetime.utcfromtimestamp(response.tx_time).replace(microsecond=0)
            break
        except Exception as error:
            if retries_count < const.MAX_RETRIES:
                print(error)
                time.sleep(const.SLEEP_TIME)
            else:
                exit(error)