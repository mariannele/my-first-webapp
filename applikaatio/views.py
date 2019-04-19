from django.shortcuts import render, redirect
import requests
from .models import Businesstrip
from .forms import BusinesstripForm #CityForm


def HomePageView(request):
    return render(request, 'home.html', {'title' : 'Home'})

def list_businesstrips(request):
    businesstrips = Businesstrip.objects.all()

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=9cbb6fbdc8d9bb39470b77dd1efed111'
    
    weather_data = []

    for city in businesstrips:
        #request the API data and convert the JSON to Python data types:
        city_weather = requests.get(url.format(city)).json()
        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }
        
        #add the data for the current city into our list:
        weather_data.append(weather)

    return render(request, 'businesstrips.html', {'businesstrips': businesstrips,
    'weather_data' : weather_data, 'title' : 'View'})

def create_businesstrip(request):
    form = BusinesstripForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_businesstrips')
    
    return render(request, 'businesstrip-form.html', {'form' : form, 'title' : 'Create'})

def update_businesstrip(request, id):
    businesstrip = Businesstrip.objects.get(id=id)
    form = BusinesstripForm(request.POST or None, instance=businesstrip)

    if form.is_valid():
        form.save()
        return redirect('list_businesstrips')

    return render(request, 'businesstrip-form.html', {'form': form, 'businesstrip': businesstrip, 'title' : 'Update'})

def delete_businesstrip(request, id):
    businesstrip = Businesstrip.objects.get(id=id)

    if request.method == 'POST':
        businesstrip.delete()
        return redirect('list_businesstrips')

    return render(request, 'businesstrip_delete.html', {'businesstrip' : businesstrip, 'title' : 'Delete'})

def weather(request):
    cities = Businesstrip.objects.all()

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=9cbb6fbdc8d9bb39470b77dd1efed111'
    
    """if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    
    form = CityForm()"""
    
    weather_data = []

    for city in cities:
        #request the API data and convert the JSON to Python data types:
        city_weather = requests.get(url.format(city)).json()
        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }
        
        #add the data for the current city into our list:
        weather_data.append(weather)

    return render(request, 'weatherview.html', {'weather_data' : weather_data})