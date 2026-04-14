#!/bin/bash

# Install dependencies
python3 -m pip install -r requirements.txt --break-system-packages

# Run migrations (Optional, but good practice if you want automatic migrations)
python3 manage.py migrate --noinput

# Collect static files
python3 manage.py collectstatic --noinput
