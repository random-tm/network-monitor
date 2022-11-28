import os

def dns_server_is_online (hostname):
    response = os.system("dig @" + hostname +" google.com" + ">/dev/null 2>&1")
    if response == 0:
        return True
    else:
        return False