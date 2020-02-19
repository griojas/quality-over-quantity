import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.middleware.proxy_fix import ProxyFix
from .config import config_by_name

db = SQLAlchemy()

def create_app():
  # create and configure the app, set minimum defaults
  app = Flask(__name__, instance_relative_config=True)

  app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

  CORS(app)

  app.config.from_object(config_by_name[os.getenv('FLASK_ENV')])
  
  db.init_app(app)
  
  migrate= Migrate(app, db)

  # Registering blueprints
  from .api import blueprint as api
  from .views import blueprint as views

  app.register_blueprint(api, url_prefix='/api')
  app.register_blueprint(views)

  return app