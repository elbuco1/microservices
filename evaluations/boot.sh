#!/bin/sh
source venv/bin/activate
flask initdb
# flask translate compile
exec gunicorn -b :5001 --access-logfile - --error-logfile - evaluations:app