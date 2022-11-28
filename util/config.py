from util.internal.json_loader import *

def get_config():
    config_data = parse_json("config.json")
    return config_data