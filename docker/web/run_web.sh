#!/bin/bash

su -m ss -c "python manage.py migrate"
su -m ss -c "gunicorn wsgi:application -w 2 -b :8000"