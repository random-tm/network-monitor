import socket
import os

def socket_is_open(hostname, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((hostname, port))
    sock.close()
    if result == 0:
        return True
    else:
        return False