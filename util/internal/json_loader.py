import json
  
def parse_json(file_name):
    f = open(file_name)
    schedule_raw = json.load(f)

    schedule_data = dict()
    for i in schedule_raw:
        schedule_data[i] = schedule_raw[i]
    
    f.close()
    return schedule_data