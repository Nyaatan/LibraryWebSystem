#!/bin/bash
set -e
cd ..
python3 -m venv --system-site-packages dist
. dist/bin/activate
pip install Django
cp -R src dist/www
cp -R books dist/books
cd dist/www
python manage.py makemigrations
python manage.py migrate
