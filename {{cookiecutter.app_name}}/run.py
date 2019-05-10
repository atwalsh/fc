from {{cookiecutter.app_slug}}.config import Config
from {{cookiecutter.app_slug}}.app import create_app

app = create_app(Config())

if __name__ == '__main__':
    app.run()
