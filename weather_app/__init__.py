from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


# Initialize app
app = Flask(__name__)

# Set SQLite database
# sqlite
# app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:////tmp/weather.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{BASE_DIR}/weather.db'

# ejemlo mysql user/pwd@ip:port/db
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://weather:weather@127.0.0.1:3306/weather'

# Turn off track modifications (it's deprecated)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Set secret key (to use messages)
app.config['SECRET_KEY'] = 'e1bc9ace66f8f5c5f4679b05e4b4c4753c33d9e08ed'

db = SQLAlchemy(app)

from weather_app import routes
