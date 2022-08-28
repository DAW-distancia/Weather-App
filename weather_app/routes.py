import requests
from flask import render_template, request
from weather_app import app, db

from .models import City


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_city = request.form.get('city')
        if new_city:
            new_city_obj = City(name=new_city)
            db.session.add(new_city_obj)
            db.session.commit()


    cities = City.query.all()
        
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=56fd34333212ace3296df963b083bd09'

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city.name)).json()
    
        data = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon':r['weather'][0]['icon']
        }

        weather_data.append(data)

    return render_template('weather.html', weather_data=weather_data)