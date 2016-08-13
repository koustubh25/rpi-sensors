import json

def get_pin_number(pin):
    json_data=open('config.json').read()
    data = json.loads(json_data)
    return data[pin]
