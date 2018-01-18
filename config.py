import os
basedir = os.path.abspath(os.path.dirname(__file__))
print("basedir", basedir)

class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY") or "ddd"
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.163.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '465'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in \
         ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', "libing775544@163.com" )
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', "a123456")
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'

    #FLASKY_MAIL_SENDER = 'Cuzz Admin <flasky@example.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URL") or \
        "sqlite:///" + os.path.join(basedir, "data-dev.sqlite")


class ProductionConfig(Config):
    pass

config = dict(
    development = DevelopmentConfig,
    production = ProductionConfig,

    default = DevelopmentConfig,
)
