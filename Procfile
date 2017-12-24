web: gunicorn translator.wsgi
web: python translator/manage.py collectstatic --noinput; gunicorn --pythonpath project translator.wsgi