import os

base_dir = os.path.dirname(os.path.abspath(__file__))


class BaseConfig:
    APP_NAME = os.getenv("APP_NAME", "Flask app")
    SECRET_KEY = os.getenv("SECRET_KEY", "secret")
    DEBUG_TB_ENABLED = False
    SQLALCHEMY_TRACK_MODIFICATION = False
    WTF_CSRF_ENABLED = False

    @staticmethod
    def configure(app):
        pass


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.egetenv("SQLALCHEMY_DATABASE_URI",
                                         "sqlite:///" + os.path.join(base_dir, "development.sqlite3"))


class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.egetenv("SQLALCHEMY_DATABASE_URI",
                                         "sqlite:///" + os.path.join(base_dir, "development.sqlite3"))
    WTF_CSRF_ENABLED = True


config = dict(development=DevelopmentConfig, production=ProductionConfig)
