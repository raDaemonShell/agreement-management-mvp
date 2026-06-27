#!/bin/bash
set -e

echo "Running migrations..."
python manage.py migrate

echo "Creating superuser..."
python create_admin.py

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting server..."
gunicorn config.wsgi --bind 0.0.0.0:10000