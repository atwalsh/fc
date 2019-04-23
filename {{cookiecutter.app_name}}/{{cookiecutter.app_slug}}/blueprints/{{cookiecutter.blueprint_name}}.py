from flask import Blueprint, render_template

{{cookiecutter.blueprint_name}} = Blueprint('{{cookiecutter.blueprint_name}}', __name__)


@{{cookiecutter.blueprint_name}}.route('/')
def index():
    return render_template('index.html', app_name='{{cookiecutter.app_name}}')