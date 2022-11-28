import socket
import struct
import sys
import time

def verify_ntp(addr):
    ntp_pool_time = get_ntp("pool.ntp.org")
    for x in range(0, 5):
        local_time = get_ntp(addr)
        max_offset = 60
        if local_time + 60 >= ntp_pool_time and local_time - 60 <= ntp_pool_time:
            return True
    return False

# Based off: https://stackoverflow.com/questions/36500197/how-to-get-time-from-an-ntp-server
def get_ntp(addr):
    try:
        REF_TIME_1970 = 2208988800  # Reference time
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client.settimeout(20)
        data = b'\x1b' + 47 * b'\0'
        client.sendto(data, (addr, 123))
        data, address = client.recvfrom(1024)
        if data:
            t = struct.unpack('!12I', data)[10]
            t -= REF_TIME_1970
        return t
    except TimeoutError:
        return 0