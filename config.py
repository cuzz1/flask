import os
basedir = os.path.abspath(os.path.dirname(__file__))
print("basedir", basedir)

class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY") or "ddd"

    @staticmethod
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
