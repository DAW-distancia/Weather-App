from flask import redirect, render_template, request, url_for

import requests

from weather_app import app
from weather_app.models import City


@app.route('/', methods=['POST'])
def index_post():
    new_city = request.form.get('city')

    if new_city:
        if not City.query.filter_by(name=new_city).first():
            # add_city_if_correct returns success message
            # if city was added
            # and failure message if not
            # message = add_city_if_correct(new_city)
            pass

    return redirect(url_for('index_get'))
        

@app.route('/', methods=['GET'])
def index_get():
    cities = City.query.all()
        
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}\
           &units=metric&appid=56fd34333212ace3296df963b083bd09'

    weather_data = []

    for city in cities:

        json_data = requests.get(url.format(city.name)).json()
    
        data = {
            'city': city.name,
            'temperature': json_data['main']['temp'],
            'description': json_data['weather'][0]['description'],
            'icon': json_data['weather'][0]['icon'],
        }

        weather_data.append(data)

    return render_template('weather.html', weather_data=weather_data)
