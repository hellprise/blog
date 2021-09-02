import requests
from django.shortcuts import render

from .models import City


def weather_app(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=de3393bc8ec07199856563ab34a89622'
    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()  # вставляем переменную city в фигурные скобки
        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon']
        }
        all_cities.append(city_info)

    context = {'all_info': city_info}
    return render(request, 'weather/weather-city.html', context)
