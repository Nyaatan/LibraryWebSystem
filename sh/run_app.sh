#!/bin/bash
set -e
cd ../dist
. bin/activate
cd www
python manage.py runserver 8008