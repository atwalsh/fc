from {{cookiecutter.app_slug}}.config import create_config
from {{cookiecutter.app_slug}}.app import create_app

config = create_config()
app = create_app(config)

if __name__ == '__main__':
    app.run()
