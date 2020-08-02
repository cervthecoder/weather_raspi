from django.shortcuts import render
#import Adafruit_DHT
import requests


def index(request):
    #sensor = Adafruit_DHT.DHT11
    #pin = 4
    #humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    humidity, temperature = 70, 25

    api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
    city = "Rynholec"
    url = api_address + city
    json_data = requests.get(url).json()
    format_add = json_data["main"]

    temperature_map = json_data['main']['temp']
    pressure_map = json_data['main']['pressure']
    humidity_map = json_data['main']['humidity']


    weather = {
        'humidity': humidity,
        'temperature': temperature,
        'temperature_map': temperature_map,
        'pressure_map': pressure_map,
        'humidity_map': humidity_map,
    }

    
    context = {'weather': weather}

    return render(request, 'weather/weather.html', context)