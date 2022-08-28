import requests
from flask import render_template
from weather_app import app, db

from .models import City


@app.route('/')
def index():
    cities = City.query.all()
        
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=56fd34333212ace3296df963b083bd09'

    weather_data = []

    for city in cities:
        
        print(city)

        r = requests.get(url.format(city)).json()

        print(r)
    
        data = {
            'city': city,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon':r['weather'][0]['icon']
        }

        weather_data.append(data)

    print(data)

    return render_template('weather.html', weather_data=weather_data)