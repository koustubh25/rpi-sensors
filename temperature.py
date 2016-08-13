from DHT11_Python import dht11
from utils import *

temperature_humidity_pin = get_pin_number('PIN_TEMPERATURE_HUMIDITY')

def get_temperature_humidity():
    instance = dht11.DHT11(temperature_humidity_pin)
    result = instance.read()
    data = {}

    if result.is_valid():
        data['temperature'] = result.temperature
        data['humidity'] = result.humidity
        data['status'] = True
    else:
        data['status'] = False
        data['error_code'] = result.error_code
    return json.dumps(data)

