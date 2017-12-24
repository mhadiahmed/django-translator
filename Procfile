web: gunicorn translator.wsgi
web: python translator/manage.py collectstatic --noinput; bin/gunicorn_django --workers=4 --bind=0.0.0.0:$PORT translator/settings 