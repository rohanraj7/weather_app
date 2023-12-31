from django.shortcuts import render
import requests 
from django.contrib import messages
from .models import City
from .forms import CityForm
# import os
from decouple import config


def index(request):


    url = config('API_URL')
    # city = 'Las Vegas'
    cities = City.objects.all().order_by('id')

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form == "":
            n = "cannot add null values"
            messages.info(request,n)
            return render(request, 'weatherapp/index.html', context) #returns the index.html template
        form.save()

    form = CityForm()

    weather_city = []

    for city in cities:

        city_weather = requests.get(url.format(city)).json()  #request the API data and convert the JSON to Python data types
        print(city_weather,"kalathilakkam award")
        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }
        print(weather,"detailssssssssssssssssss_formattting")
        weather_city.append(weather)
    context = {'weather_data' : weather_city, 'form': form}
    return render(request, 'weatherapp/index.html', context) #returns the index.html template
