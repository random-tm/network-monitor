import os

def file_can_be_downloaded (remote_file_path):
    filename = remote_file_path.split("/")[len(remote_file_path.split()) - 2]
    command = "wget " + remote_file_path + " -O /tmp/" + filename + " >/dev/null 2>&1 && rm /tmp/" + filename
    response = os.system(command)
    if response == 0:
        return True
    else:
        return False