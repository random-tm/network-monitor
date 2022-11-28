import time
import os
from util.schedule import *
from util.email import *
from util.config import *

schedule = get_schedule()
config = get_config()

hour_counter = 0

def should_execute(file_name):
    if not file_name in schedule:
        return True
    file_hour_schedule = schedule[file_name]
    if hour_counter % file_hour_schedule == 0:
        return True
    return False

def get_tasks():
    top_level_directory = []
    tasks_path = "./tasks"
    for (dirpath, dirnames, filenames) in os.walk(tasks_path):
        top_level_directory.extend(filenames)
        break
    return top_level_directory

def execute_tasks():
    tasks = get_tasks()
    failed_tasks = []
    for task in tasks:
        if should_execute(task):
            command = config["python_binary"] + " ./tasks/" + task
            status_code = os.system(command)
            if status_code != 0:
                failed_tasks.append(task)
    return failed_tasks

def notify_failure(failed_tasks):
    send_email(failed_tasks)

has_error = False

while True:
    hour_seconds = 60 * 60
    failed_tasks = execute_tasks()
    if has_error == False and len(failed_tasks) != 0:
        notify_failure(failed_tasks)
    if len(failed_tasks) == 0:
        has_error = False
    else:
        has_error = True
    time.sleep(hour_seconds)
    hour_counter += 1
