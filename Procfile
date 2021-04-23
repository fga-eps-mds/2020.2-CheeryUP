release: heroku run bash && --pythonpath src python manage.py migrate
web: gunicorn --pythonpath src CheerUp.wsgi
