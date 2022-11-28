from util.internal.json_loader import *

def get_schedule():
    schedule_data = parse_json("schedule.json")
    return schedule_data