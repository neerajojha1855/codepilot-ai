web: gunicorn CodePilot.wsgi:application --log-file -
worker: python manage.py qcluster
release: python manage.py migrate
