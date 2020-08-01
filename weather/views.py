from django.shortcuts import render
import Adafruit_DHT


def index(request):
    sensor = Adafruit_DHT.DHT11
    pin = 4
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    humidity, temperature = 60, 20

    weather = {
        'humidity': humidity,
        'temperature': temperature,
    }

    context = {'weather': weather}

    return render(request, 'weather/weather.html', context)