from models import Temp
import Adafruit_DHT
from datetime import datetime
import time

def get_time():
    return f'{datetime.now().hour}:{datetime.now().minute}'

def get_temp_hum():
    sensor = Adafruit_DHT.DHT11
    pin = 4
    return Adafruit_DHT.read_retry(sensor, pin)

def main():
    while True:
        if datetime.now().minute == 0 and datetime.now().second == 0:
            humidity, temperature = get_temp_hum()
            Temp(temperature=temperature, humidity=humidity, time=get_time(), month=datetime.now().month).save()
            time.sleep(1)

# will be run through wsgi.py



