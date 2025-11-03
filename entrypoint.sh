#!/bin/bash
set -e

echo "Ensuring staticfiles directory exists..."
mkdir -p /usr/src/app/staticfiles

echo "Running Django collectstatic..."
python manage.py collectstatic --noinput

echo "Starting the Django server..."
exec "$@"
