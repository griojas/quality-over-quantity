import os, sys

basedir = os.path.abspath(os.path.dirname(__file__))
parentdir = os.path.abspath(os.path.join(basedir, os.pardir))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///' + os.path.join(parentdir, 'qt.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class TestConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI')

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI')
    
config_by_name = dict(
    development=DevelopmentConfig,
    test=TestConfig,
    production=ProductionConfig
)

key = Config.SECRET_KEY