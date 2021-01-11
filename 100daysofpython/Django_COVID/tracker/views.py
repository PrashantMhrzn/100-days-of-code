from django.shortcuts import render
import requests

def home(request):
    result = requests.get('https://nepalcorona.info/api/v1/data/nepal')
    data = result.json()
    return render(request, 'tracker/home.html', {'data': data})
