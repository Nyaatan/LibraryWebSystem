#!/bin/bash
set -e
cd ..
python3 -m venv --system-site-packages dist
. dist/bin/activate
pip install Django
cp -R src dist/www
cd dist/www
python manage.py makemigrations
python manage.py migrate
