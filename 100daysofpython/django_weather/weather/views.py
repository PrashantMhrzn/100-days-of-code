from django.shortcuts import render
from django.http import HttpResponse
import requests

res = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat=27.6981&lon=85.3592&exclude=hourly,daily,minutely,alerts&units=metric&appid={YOURAPIKEY}')
data = res.json()

def home(request):
    return render(request, 'weather/home.html', {'data': data})
