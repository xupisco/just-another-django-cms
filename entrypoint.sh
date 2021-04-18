#!/bin/sh

# python manage.py flush --no-input
python manage.py migrate
yarn install --non-interactive --no-progress --ignore-optional

exec "$@"
