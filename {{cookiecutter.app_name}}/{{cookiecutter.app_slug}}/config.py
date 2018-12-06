import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
{% if cookiecutter.db == "PostgreSQL" %}
postegres_uri_template = 'postgresql://{}:{}@{}:{}/{}'
{% endif %}

class Config:
    def __init__(self):
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    def __init__(self):
        super(DevelopmentConfig, self).__init__()
        self.DEBUG = True
        self.ENV = 'development'
        {% if cookiecutter.db == "PostgreSQL" %}
        self.SQLALCHEMY_DATABASE_URI = postegres_uri_template.format(
            os.environ['DEV_DB_USERNAME'],
            os.environ['DEV_DB_PASSWORD'],
            os.environ['DEV_DB_ADDRESS'],
            os.environ['DEV_DB_PORT'],
            os.environ['DEV_DB_NAME']
        )
        {% elif cookiecutter.db == "SQLite (memory)" %}
        self.SQLALCHEMY_DATABASE_URI = 'sqlite:///../{{ cookiecutter.app_slug }}.db'
        {% endif %}

{% if cookiecutter.db == "SQLite (memory)" %}
class MigrationConfig(DevelopmentConfig):
    def __init__(self):
        super(MigrationConfig, self).__init__()
        self.SQLALCHEMY_DATABASE_URI = 'sqlite:///{{ cookiecutter.app_slug }}.db'

{% endif %}
class ProductionConfig(Config):
    def __init__(self):
        super(ProductionConfig, self).__init__()
        {% if cookiecutter.db == "PostgreSQL" %}
        self.SQLALCHEMY_DATABASE_URI = postegres_uri_template.format(
            os.environ['DB_USERNAME'],
            os.environ['DB_PASSWORD'],
            os.environ['DB_ADDRESS'],
            os.environ['DB_PORT'],
            os.environ['DB_NAME']
        )
        {% elif cookiecutter.db == "SQLite (memory)" %}
        self.SQLALCHEMY_DATABASE_URI = 'sqlite:///../{{ cookiecutter.app_slug }}.db'
        {% endif %}

def create_config() -> Config:
    if os.getenv('DEV') == '1':
        return DevelopmentConfig()
    else:
        return ProductionConfig()
