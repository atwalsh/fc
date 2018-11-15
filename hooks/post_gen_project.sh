#!/usr/bin/env bash

# Add .env
touch {{cookiecutter.app_slug}}/.env
echo "DEV=1" > {{cookiecutter.app_slug}}/.env
