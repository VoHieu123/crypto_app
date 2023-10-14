import ntplib
from datetime import datetime
from time import ctime
import uuid

def generate_uuid():
    return str(uuid.uuid4())

def synchronize_time():
    ntp_server = 'pool.ntp.org'  # Use a reliable NTP server

    client = ntplib.NTPClient()
    response = client.request(ntp_server)

    # Update the system time with the NTP server's time
    datetime.utcfromtimestamp(response.tx_time).replace(microsecond=0)

    print("NTP server time:", ctime(response.tx_time))
    print("System time updated:", ctime())