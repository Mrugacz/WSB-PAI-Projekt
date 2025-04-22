import os


class Config(object):
    PORT=os.environ['APP_PORT']
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ['APP_SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = os.environ['APP_DATABASE_URL']


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    PORT=os.environ['APP_TEST_PORT']
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    WTF_CSRF_ENABLED = False