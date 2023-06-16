from flask import Flask
from config import Config
from flask_migrate import Migrate
from flask_cors import CORS

from .api.routes import api
from .models import db

app = Flask(__name__)
CORS(app, origins='https://behind-the-madiverse.onrender.com')

app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)




app.register_blueprint(api)


from . import routes