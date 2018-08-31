from flask_migrate import MigrateCommand
from flask_script import Manager

from {{cookiecutter.app_slug}}.app import create_app
from {{cookiecutter.app_slug}}.config import create_config

app = create_app(config=create_config())

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
