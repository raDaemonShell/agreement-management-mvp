#!/bin/sh

python manage.py migrate
python create_admin.py

exec gunicorn config.wsgi:application --bind 0.0.0.0:10000