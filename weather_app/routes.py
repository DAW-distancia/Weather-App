from flask import flash, redirect, render_template, request, url_for

import requests

from weather_app import app, db
from weather_app.models import City


def get_weather_data(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ city }\
            &units=metric&appid=271d1234d3f497eed5b1d80a07b3fcd1'
    data_json = requests.get(url).json()
    return data_json


@app.route('/', methods=['POST'])
def index_post():
    # Lower form input to avoid duplicates in db
    new_city = (request.form.get('city')).lower()

    err_msg = None

    # Check if theres anything in the form
    if new_city:
        # Check if city already exists in database
        if not City.query.filter_by(name=new_city).first():
            # Check if city entered correctly
            if get_weather_data(new_city)['cod'] == 200:
                db.session.add(City(name=new_city))
                db.session.commit()
            else:
                err_msg = 'Incorrect city name. Please try again'
        else:
            err_msg = 'This city is already added'

    if err_msg:
        flash(err_msg, 'error')
    else:
        flash('City added succesfully!')

    return redirect(url_for('index_get'))
        

@app.route('/', methods=['GET'])
def index_get():
    cities = City.query.all()

    weather_data = []

    for city in cities:

        json_data = get_weather_data(city)
    
        data = {
            'city': city.name,
            'temperature': json_data['main']['temp'],
            # Capitalize to make it look better
            'description': json_data['weather'][0]['description'].capitalize(),
            'icon': json_data['weather'][0]['icon'],
        }

        weather_data.append(data)

    return render_template(
        'weather.html',
        # Reverse list to get newly added cities first
        weather_data=reversed(weather_data),
    )


@app.route('/delete/<name>')
def delete_city(name):
    city = City.query.filter_by(name=name).first()
    db.session.delete(city)
    db.session.commit()

    flash(f'Successfully deleted { city.name }', 'success')
    return redirect(url_for('index_get'))
