import os

def file_can_be_downloaded (remote_file_path):
    filename = remote_file_path.split("/")[len(remote_file_path.split()) - 2]
    params = "--retry-connrefused --waitretry=1 --read-timeout=20 --timeout=15 -t 5"
    command = "wget " + params + " " + remote_file_path + " -O /tmp/" + filename + " >/dev/null 2>&1 && rm /tmp/" + filename
    response = os.system(command)
    if response == 0:
        return True
    else:
        return False