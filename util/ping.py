import os

def host_is_online (hostname):
    response = os.system("ping -c 1 " + hostname + " >/dev/null 2>&1")
    if response == 0:
        return True
    else:
        return False