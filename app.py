import requests
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def index():
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=56fd34333212ace3296df963b083bd09'
    city = 'Las Vegas'

    r = requests.get(url.format(city)).json()
    
    data = {
        'city': city,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon':r['weather'][0]['icon']
    }

    print(data)

    return render_template('weather.html', data=data)