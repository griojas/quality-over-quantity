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
    JIRA_SERVER_URL=os.getenv('JIRA_SERVER_URL','')
    JIRA_USER=os.getenv('JIRA_USER', '')
    JIRA_API_KEY=os.getenv('JIRA_API_KEY', '')
    JIRA_DEFAULT_FIELDS=os.getenv('JIRA_DEFAULT_FIELDS', 'project,key,issuetype,fixVersions,labels,created,resolution,resolutiondate,status,summary,customfield_10835,customfield_10836,worklog,customfield_10007')
    
    

class TestConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///' + os.path.join(parentdir, 'qt.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JIRA_SERVER_URL=os.getenv('JIRA_SERVER_URL','')
    JIRA_USER=os.getenv('JIRA_USER', '')
    JIRA_API_KEY=os.getenv('JIRA_API_KEY', '')
    JIRA_DEFAULT_FIELDS=os.getenv('JIRA_DEFAULT_FIELDS', 'project,key,issuetype,fixVersions,labels,created,resolution,resolutiondate,status,summary,customfield_10835,customfield_10836,worklog,customfield_10007')
    

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI')
    JIRA_SERVER_URL=os.getenv('JIRA_SERVER_URL')
    JIRA_USER=os.getenv('JIRA_USER')
    JIRA_API_KEY=os.getenv('JIRA_API_KEY')
    JIRA_DEFAULT_FIELDS=os.getenv('JIRA_DEFAULT_FIELDS')

config_by_name = dict(
    development=DevelopmentConfig,
    test=TestConfig,
    production=ProductionConfig
)

key = Config.SECRET_KEY